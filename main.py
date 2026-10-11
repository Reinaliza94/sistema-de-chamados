from flask import Flask, render_template, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
app = Flask(__name__)

from models import chamado, usuario, tecnico
from models.conexao import engine

Session = sessionmaker(bind=engine)