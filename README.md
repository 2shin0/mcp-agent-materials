# AI Agent 및 데이터 분석 실습 자료

이 저장소는 **AI Agent 개발**, **데이터 수집 및 분석**, 그리고 **챗봇 제작 및 배포**에 이르는 일련의 과정을 실습할 수 있도록 구성되어 있습니다.

최종 결과물은 아래 레포지토리에서 확인하실 수 있습니다.

[MCP Server](https://github.com/2shin0/youtube-mcp-server)

[MCP Client](https://github.com/2shin0/youtube-chat)

## 환경 설정 및 필수 파일

| 파일/폴더 | 설명 | 설정 방법 |
| :--- | :--- | :--- |
| *.env.example** | 환경 변수 설정 파일의 예시입니다. | 이 파일을 복사하여 *.env** 파일을 생성하고, **YouTube** 및 **Gemini API Key**를 발급받아 붙여넣으세요. |
| *requirements.txt** | 프로젝트에 필요한 라이브러리 목록입니다. | 다음 코드를 사용하여 **가상 환경**을 설정하고 패키지들을 다운로드하세요: <br> python -m venv venv <br> source venv/bin/activate (Linux/macOS) 또는 .\venv\Scripts\activate (Windows) <br> pip install -r requirements.txt |

## 📚 실습 자료 구성 (4단계 워크플로우)

### 1\. streamlit 폴더: AI Agent 개념 및 개발 환경 세팅

AI Agent의 기초 지식 습득과 개발 환경 설정을 목표로 합니다.

  * **1-1 AI Agent 기초:** AI Agent의 기본 개념 학습

  * **1-2 개발 환경 준비:** 필요한 도구 및 환경 설정

  * **1-3 Streamlit 기초:** 웹 애플리케이션 프레임워크 Streamlit 기본 사용법

  * **1-4 Gemini API 연동하기:** Gemini API를 활용한 연동 방법 (GPT API 소개 포함)

  * **1-5 실습:** **기본 챗봇** 개발 (Gemini API 연동하여 Streamlit으로 띄워보기)

### 2\. mcp 폴더: 데이터 수집

YouTube 데이터 수집에 필요한 기초 지식 및 **MCP(Multi-Channel Processing)** 활용법을 다룹니다.

  * **2-1 데이터 수집 기초:** 데이터 수집의 기본 개념

  * **2-2 MCP를 활용한 유튜브 데이터 수집:** MCP 도구를 사용한 유튜브 데이터 수집 방법

  * **2-3 실습:** **API와 MCP**를 활용한 유튜브 데이터 수집

  * **2-4 데이터 스트리밍 & 스케줄링:** 실시간 데이터 처리 및 작업 자동화 개념

  * **2-5 실습:** **데이터 스케줄링**을 활용한 유튜브 데이터 수집

### 3\. data 폴더: 데이터 분석

수집된 데이터를 탐색하고 분석하는 과정을 **프롬프트 엔지니어링**과 함께 실습합니다.

  * **3-1 데이터 분석 기초:** 데이터 분석의 기본 원리 및 방법

  * **3-2 실습:** \*\*탐색적 데이터 분석(EDA)\*\*와 텍스트 전처리

  * **3-3 데이터 분석기:** 데이터 분석을 위한 도구 및 라이브러리 소개

  * **3-4 실습:** **프롬프트 엔지니어링** 기초 및 적용

  * **3-5 실습:** **뉴스 데이터 자동 분석 & 요약 스크립트** 제작

### 4\. deploy 폴더: 챗봇 제작 및 배포

개발한 챗봇을 완성하고 실제 환경에 배포하는 과정을 실습합니다.

  * **4-1 챗봇 화면 설계:** 사용자 친화적인 챗봇 인터페이스 설계

  * **4-2 배포의 개념:** 개발된 애플리케이션을 서비스할 수 있게 만드는 과정 학습

  * **4-3 실습:** **뉴스 트렌드 챗봇 완성 및 배포**

---

# AI Agent and Data Analysis Workshop Materials

This repository is designed for hands-on practice covering the entire workflow of **AI Agent Development**, **Data Collection & Analysis**, and **Chatbot Creation & Deployment**.

You can find the final deliverables in the repositories below:

[MCP Server](https://github.com/2shin0/youtube-mcp-server)

[MCP Client](https://github.com/2shin0/youtube-chat)

## Environment Setup & Essential Files

| File/Folder | Description | Setup Method |
| :--- | :--- | :--- |
| **.env.example** | An example file for environment variable configuration. | Copy this file to create a **.env** file, then issue and paste your **YouTube** and **Gemini API Keys**. |
| **requirements.txt** | A list of libraries required for the project. | Use the following code to set up a **virtual environment** and download the packages: <br> `python -m venv venv` <br> `source venv/bin/activate` (Linux/macOS) or `.\venv\Scripts\activate` (Windows) <br> `pip install -r requirements.txt` |

## Workshop Structure (4-Stage Workflow)

### 1. streamlit folder: AI Agent Concepts & Development Environment Setup

Aims to acquire basic knowledge of AI Agents and set up the development environment.

* **1-1 AI Agent Basics:** Learning the fundamental concepts of AI Agents
* **1-2 Environment Preparation:** Setting up necessary tools and environments
* **1-3 Streamlit Basics:** Basic usage of the web application framework, Streamlit
* **1-4 Gemini API Integration:** How to integrate using the Gemini API (includes GPT API introduction)
* **1-5 Lab:** Developing a **Basic Chatbot** (Integrating Gemini API and launching it with Streamlit)

### 2. mcp folder: Data Collection

Covers the basic knowledge required for YouTube data collection and how to utilize **MCP (Multi-Channel Processing)**.

* **2-1 Data Collection Basics:** Fundamental concepts of data collection
* **2-2 YouTube Data Collection with MCP:** How to collect YouTube data using MCP tools
* **2-3 Lab:** YouTube data collection using **API and MCP**
* **2-4 Data Streaming & Scheduling:** Concepts of real-time data processing and task automation
* **2-5 Lab:** YouTube data collection using **Data Scheduling**

### 3. data folder: Data Analysis

Practice exploring and analyzing collected data alongside **Prompt Engineering**.

* **3-1 Data Analysis Basics:** Basic principles and methods of data analysis
* **3-2 Lab:** **Exploratory Data Analysis (EDA)** and Text Preprocessing
* **3-3 Data Analyzer:** Introduction to tools and libraries for data analysis
* **3-4 Lab:** **Prompt Engineering** Basics & Application
* **3-5 Lab:** Creating an **Automated News Data Analysis & Summary Script**

### 4. deploy folder: Chatbot Creation & Deployment

Practice finalizing the developed chatbot and deploying it to a live environment.

* **4-1 Chatbot UI Design:** Designing a user-friendly chatbot interface
* **4-2 Deployment Concepts:** Learning the process of making a developed application serviceable
* **4-3 Lab:** **News Trend Chatbot Completion & Deployment**
