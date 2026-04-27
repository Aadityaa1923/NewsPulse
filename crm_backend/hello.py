Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\WINDOWS\system32> pip install fastapi uvicorn request sqlalchemy psycopg2-binary textblon
Collecting fastapi
  Downloading fastapi-0.136.1-py3-none-any.whl.metadata (28 kB)
Collecting uvicorn
  Downloading uvicorn-0.46.0-py3-none-any.whl.metadata (6.7 kB)
ERROR: Could not find a version that satisfies the requirement request (from versions: none)

[notice] A new release of pip is available: 25.1.1 -> 26.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip
ERROR: No matching distribution found for request
PS C:\WINDOWS\system32> python -m pip install --upgrade pip
Requirement already satisfied: pip in c:\users\aadityaa\appdata\local\programs\python\python312\lib\site-packages (25.1.1)
Collecting pip
  Downloading pip-26.0.1-py3-none-any.whl.metadata (4.7 kB)
Downloading pip-26.0.1-py3-none-any.whl (1.8 MB)
   ---------------------------------------- 1.8/1.8 MB 10.9 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 25.1.1
    Uninstalling pip-25.1.1:
      Successfully uninstalled pip-25.1.1
Successfully installed pip-26.0.1
PS C:\WINDOWS\system32> python -m pip install fastapi
Collecting fastapi
  Using cached fastapi-0.136.1-py3-none-any.whl.metadata (28 kB)
Collecting starlette>=0.46.0 (from fastapi)
  Downloading starlette-1.0.0-py3-none-any.whl.metadata (6.3 kB)
Requirement already satisfied: pydantic>=2.9.0 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from fastapi) (2.11.4)
Requirement already satisfied: typing-extensions>=4.8.0 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from fastapi) (4.13.2)
Collecting typing-inspection>=0.4.2 (from fastapi)
  Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting annotated-doc>=0.0.2 (from fastapi)
  Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
Requirement already satisfied: annotated-types>=0.6.0 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from pydantic>=2.9.0->fastapi) (0.7.0)
Requirement already satisfied: pydantic-core==2.33.2 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from pydantic>=2.9.0->fastapi) (2.33.2)
Requirement already satisfied: anyio<5,>=3.6.2 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from starlette>=0.46.0->fastapi) (4.9.0)
Requirement already satisfied: idna>=2.8 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from anyio<5,>=3.6.2->starlette>=0.46.0->fastapi) (3.10)
Requirement already satisfied: sniffio>=1.1 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from anyio<5,>=3.6.2->starlette>=0.46.0->fastapi) (1.3.1)
Downloading fastapi-0.136.1-py3-none-any.whl (117 kB)
Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
Downloading starlette-1.0.0-py3-none-any.whl (72 kB)
Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Installing collected packages: typing-inspection, annotated-doc, starlette, fastapi
  Attempting uninstall: typing-inspection
    Found existing installation: typing-inspection 0.4.0
    Uninstalling typing-inspection-0.4.0:
      Successfully uninstalled typing-inspection-0.4.0
Successfully installed annotated-doc-0.0.4 fastapi-0.136.1 starlette-1.0.0 typing-inspection-0.4.2
PS C:\WINDOWS\system32> python -m pip install uvicorn
Collecting uvicorn
  Using cached uvicorn-0.46.0-py3-none-any.whl.metadata (6.7 kB)
Requirement already satisfied: click>=7.0 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from uvicorn) (8.1.8)
Requirement already satisfied: h11>=0.8 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from uvicorn) (0.16.0)
Requirement already satisfied: colorama in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from click>=7.0->uvicorn) (0.4.6)
Downloading uvicorn-0.46.0-py3-none-any.whl (70 kB)
Installing collected packages: uvicorn
Successfully installed uvicorn-0.46.0
PS C:\WINDOWS\system32> python -m pip install requests
Requirement already satisfied: requests in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (2.32.3)
Requirement already satisfied: charset-normalizer<4,>=2 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from requests) (3.4.1)
Requirement already satisfied: idna<4,>=2.5 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from requests) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from requests) (2.4.0)
Requirement already satisfied: certifi>=2017.4.17 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from requests) (2025.1.31)
PS C:\WINDOWS\system32> python -m pip install sqlalchemy
Requirement already satisfied: sqlalchemy in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (2.0.41)
Requirement already satisfied: greenlet>=1 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from sqlalchemy) (3.2.2)
Requirement already satisfied: typing-extensions>=4.6.0 in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from sqlalchemy) (4.13.2)
PS C:\WINDOWS\system32> python -m pip install textblob
Collecting textblob
  Downloading textblob-0.20.0-py3-none-any.whl.metadata (4.0 kB)
Collecting nltk>=3.9 (from textblob)
  Downloading nltk-3.9.4-py3-none-any.whl.metadata (3.2 kB)
Requirement already satisfied: click in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from nltk>=3.9->textblob) (8.1.8)
Collecting joblib (from nltk>=3.9->textblob)
  Downloading joblib-1.5.3-py3-none-any.whl.metadata (5.5 kB)
Collecting regex>=2021.8.3 (from nltk>=3.9->textblob)
  Downloading regex-2026.4.4-cp312-cp312-win_amd64.whl.metadata (41 kB)
Requirement already satisfied: tqdm in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from nltk>=3.9->textblob) (4.67.1)
Requirement already satisfied: colorama in C:\Users\Aadityaa\AppData\Local\Programs\Python\Python312\Lib\site-packages (from click->nltk>=3.9->textblob) (0.4.6)
Downloading textblob-0.20.0-py3-none-any.whl (624 kB)
   ---------------------------------------- 625.0/625.0 kB 7.7 MB/s  0:00:00
Downloading nltk-3.9.4-py3-none-any.whl (1.6 MB)
   ---------------------------------------- 1.6/1.6 MB 10.3 MB/s  0:00:00
Downloading regex-2026.4.4-cp312-cp312-win_amd64.whl (277 kB)
Downloading joblib-1.5.3-py3-none-any.whl (309 kB)
Installing collected packages: regex, joblib, nltk, textblob
Successfully installed joblib-1.5.3 nltk-3.9.4 regex-2026.4.4 textblob-0.20.0
PS C:\WINDOWS\system32> python -m pip install psycopg2-binary
Collecting psycopg2-binary
  Downloading psycopg2_binary-2.9.12-cp312-cp312-win_amd64.whl.metadata (5.1 kB)
Downloading psycopg2_binary-2.9.12-cp312-cp312-win_amd64.whl (2.8 MB)
   ---------------------------------------- 2.8/2.8 MB 9.4 MB/s  0:00:00
Installing collected packages: psycopg2-binary
Successfully installed psycopg2-binary-2.9.12
PS C:\WINDOWS\system32> python
Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import fastapi
>>> import sqlalchemy
>>> import textblob
>>> print("OK")
OK
>>>