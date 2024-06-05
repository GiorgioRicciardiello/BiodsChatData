""""
SQL agent chatbot to talk with our uploaded files
"""
import os
from typing import List, Tuple
from .load_config import LoadConfig
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from langchain_community.agent_toolkits import create_sql_agent
import langchain
langchain.debug = True

APPCFG = LoadConfig()


class ChatBot:
    """
    A ChatBot class capable of responding to messages using different modes of operation.
    It can interact with SQL databases, leverage language chain agents for Q&A,
    and use embeddings for Retrieval-Augmented Generation (RAG) with ChromaDB.
    """
    @staticmethod
    def respond(chatbot: List,
                message: str,
                ) -> Tuple:
        """
        Respond to a message based on the given chat

        Args:
            chatbot (List): A list representing the chatbot's conversation history.
            message (str): The user's input message to the chatbot.


        Returns:
            Tuple[str, List, Optional[Any]]: A tuple containing an empty string, the updated chatbot conversation list,
                                             and an optional 'None' value. The empty string and 'None' are placeholder
                                             values to match the required return type and may be updated for further
                                             functionality.
                                             Currently, the function primarily updates the chatbot conversation list.
        """

        # If we want to use langchain agents for Q&A with our SQL DBs that were created from CSV/XLSX files.
        if os.path.exists(APPCFG.stored_csv_xlsx_sqldb_directory):
            engine = create_engine(
                f"sqlite:///{APPCFG.stored_csv_xlsx_sqldb_directory}")
            db = SQLDatabase(engine=engine)
        else:
            chatbot.append(
                (message, f"SQL DB from the stored csv/xlsx files does not exist. Please first execute "
                          f"`src/prepare_csv_xlsx_sqlitedb.py` module."))
            return "", chatbot, None
        print(db.dialect)
        print(db.get_usable_table_names())
        agent_executor = create_sql_agent(
            APPCFG.langchain_llm, db=db, agent_type="openai-tools", verbose=True)
        response = agent_executor.invoke({"input": message})
        response = response["output"]
        # Get the `response` variable from any of the selected scenarios and pass it to the user.
        chatbot.append(
            (message, response))
        return "", chatbot
