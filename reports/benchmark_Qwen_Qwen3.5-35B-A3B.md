# Qwen/Qwen3.5-35B-A3B Performance Benchmark Report

## Test Information

- **Test Time**: 2026-02-26 21:56:22
- **Model**: Qwen/Qwen3.5-35B-A3B
- **API URL**: http://localhost:8000/v1/chat/completions
- **Test Cases**: 10
- **Test Mode**: Complex Comprehensive

## GPU Information

- **Model**: NVIDIA RTX PRO 6000 Blackwell Workstation Edition
- **Memory**: 97887 MB
- **Driver**: 580.126.09
- **Peak Memory (est.)**: N/A

## Test Results Summary

| Metric | Value |
|--------|-------|
| Successful Tests | 10/10 |
| **Avg Generation Speed** | **157.1 tok/s** |
| Total Time | 48.34s |
| Total Tokens | 6600 |

### Speed Statistics

- **Max**: 169.0 tok/s
- **Min**: 57.7 tok/s
- **Median**: 168.2 tok/s

## Detailed Results

| Test Case | Time | Prompt | Completion | Speed |
|-----------|------|--------|------------|-------|
| Full Backend System | 13.87s | 92 | 800 | **57.7** tok/s |
| Microservices Architecture | 3.58s | 101 | 600 | **167.6** tok/s |
| Complex Algorithms | 4.14s | 56 | 700 | **169.0** tok/s |
| Debug Task | 2.99s | 166 | 500 | **167.3** tok/s |
| Data Analysis Report | 3.57s | 112 | 600 | **168.2** tok/s |
| System Design Interview | 3.56s | 92 | 600 | **168.6** tok/s |
| Multi-turn Conversation | 4.74s | 142 | 800 | **168.6** tok/s |
| Technical Documentation | 4.15s | 88 | 700 | **168.8** tok/s |
| Database Optimization | 2.99s | 133 | 500 | **167.4** tok/s |
| ML Project | 4.76s | 142 | 800 | **168.2** tok/s |

## Test Details

### Full Backend System

- **Time**: 13.87s
- **Speed**: 57.7 tok/s
- **TTFT (est.)**: 1.387s

**Response Preview:**
```
This is a comprehensive request for a FastAPI REST API with authentication, CRUD operations, database, testing, and Docker. I'll create a complete, well-structured project with all the necessary files.

Let me organize the project structure:
```
blog_api/
├── app/
│   ├── __init__.py
│   ├── main.py...
```

---

### Microservices Architecture

- **Time**: 3.58s
- **Speed**: 167.6 tok/s
- **TTFT (est.)**: 0.358s

**Response Preview:**
```
Here's a thinking process that leads to the suggested microservices architecture:

1.  **Deconstruct the Request:**
    *   **Topic:** Microservices Architecture for an E-commerce Platform.
    *   **Required Components:**
        1.  Service Breakdown (User, Catalog, Order, Payment, Inventory, Noti...
```

---

### Complex Algorithms

- **Time**: 4.14s
- **Speed**: 169.0 tok/s
- **TTFT (est.)**: 0.414s

**Response Preview:**
```
This is a comprehensive request that requires me to implement two fundamental pathfinding algorithms (A* and Dijkstra's), compare their time complexity, and provide visualization examples and test cases.

Let me break this down:

1. A* Algorithm Implementation
   - Needs a priority queue
   - Needs ...
```

---

### Debug Task

- **Time**: 2.99s
- **Speed**: 167.3 tok/s
- **TTFT (est.)**: 0.299s

**Response Preview:**
```
Let me analyze this Python code for a concurrent web scraper to identify all bugs:

1. **Main Bug - Sequential Execution**: The `t.join()` call is inside the loop, which means each thread is started and then immediately joined before starting the next one. This defeats the purpose of threading and m...
```

---

### Data Analysis Report

- **Time**: 3.57s
- **Speed**: 168.2 tok/s
- **TTFT (est.)**: 0.357s

**Response Preview:**
```
This is a comprehensive request for a retail sales analysis pipeline. I need to create a complete Python solution that covers all the mentioned tasks. Let me structure this properly with:

1. Data loading and cleaning
2. Exploratory data analysis
3. Sales trend analysis
4. Category performance analy...
```

---

### System Design Interview

- **Time**: 3.56s
- **Speed**: 168.6 tok/s
- **TTFT (est.)**: 0.356s

**Response Preview:**
```
Here's a thinking process that leads to the suggested design for a URL shortening service:

1.  **Deconstruct the Request:**
    *   **Goal:** Design a URL shortening service (like bit.ly).
    *   **Components Required:**
        1.  API Endpoints (RESTful)
        2.  Database Schema
        3.  H...
```

---

### Multi-turn Conversation

- **Time**: 4.74s
- **Speed**: 168.6 tok/s
- **TTFT (est.)**: 0.474s

**Response Preview:**
```
Thinking Process:

1.  **Analyze the Request:**
    *   **Role:** Senior Software Engineer.
    *   **Task:** Continue a debugging conversation about a slow Python app in production.
    *   **Context:** The user has a Python app, slow response times (2-5s for simple queries), database queries (SELE...
```

---

### Technical Documentation

- **Time**: 4.15s
- **Speed**: 168.8 tok/s
- **TTFT (est.)**: 0.415s

**Response Preview:**
```
Here's a thinking process that leads to the suggested documentation:

1.  **Analyze the Request:**
    *   **Topic:** Python CLI tool for image compression.
    *   **Features:** Supports PNG, JPEG, WebP; Batch processing; Quality control; Output statistics.
    *   **Required Sections:** Installati...
```

---

### Database Optimization

- **Time**: 2.99s
- **Speed**: 167.4 tok/s
- **TTFT (est.)**: 0.299s

**Response Preview:**
```
This is a comprehensive database optimization question. Let me analyze this systematically:

1. **Performance Issues Analysis:**
   - The query uses a subquery in IN clause which can be inefficient
   - SELECT * retrieves unnecessary columns
   - Missing proper indexes
   - The subquery might return...
```

---

### ML Project

- **Time**: 4.76s
- **Speed**: 168.2 tok/s
- **TTFT (est.)**: 0.476s

**Response Preview:**
```
This is a comprehensive request for building a complete ML pipeline for customer churn prediction. I need to create a production-ready codebase that covers all 8 requirements. Let me structure this properly:

1. **Exploratory Data Analysis (EDA)** - Understanding the data distribution, correlations,...
```

---


## Conclusion

**Performance Rating**: Excellent

- Average Speed: 157.1 tok/s

---
*Generated by benchmark script*
