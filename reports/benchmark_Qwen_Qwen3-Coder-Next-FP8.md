# Qwen/Qwen3.5-35B-A3B Performance Benchmark Report

## Test Information

- **Test Time**: 2026-02-26 00:50:24
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
| **Avg Generation Speed** | **153.1 tok/s** |
| Total Time | 68.60s |
| Total Tokens | 6600 |

### Speed Statistics

- **Max**: 169.2 tok/s
- **Min**: 23.5 tok/s
- **Median**: 168.4 tok/s

## Detailed Results

| Test Case | Time | Prompt | Completion | Speed |
|-----------|------|--------|------------|-------|
| Full Backend System | 33.99s | 92 | 800 | **23.5** tok/s |
| Microservices Architecture | 3.58s | 101 | 600 | **167.4** tok/s |
| Complex Algorithms | 4.14s | 56 | 700 | **169.2** tok/s |
| Debug Task | 2.98s | 166 | 500 | **167.6** tok/s |
| Data Analysis Report | 3.72s | 112 | 600 | **161.3** tok/s |
| System Design Interview | 3.56s | 92 | 600 | **168.7** tok/s |
| Multi-turn Conversation | 4.75s | 142 | 800 | **168.4** tok/s |
| Technical Documentation | 4.15s | 88 | 700 | **168.6** tok/s |
| Database Optimization | 2.98s | 133 | 500 | **167.5** tok/s |
| ML Project | 4.75s | 142 | 800 | **168.6** tok/s |

## Test Details

### Full Backend System

- **Time**: 33.99s
- **Speed**: 23.5 tok/s
- **TTFT (est.)**: 3.399s

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
- **Speed**: 167.4 tok/s
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
- **Speed**: 169.2 tok/s
- **TTFT (est.)**: 0.414s

**Response Preview:**
```
This is a comprehensive request that requires me to implement two classic pathfinding algorithms (A* and Dijkstra's), compare their time complexity, and provide visualization examples and test cases. Let me structure this well with detailed comments.

I'll need to:
1. Implement A* algorithm with heu...
```

---

### Debug Task

- **Time**: 2.98s
- **Speed**: 167.6 tok/s
- **TTFT (est.)**: 0.298s

**Response Preview:**
```
Let me analyze this Python code for a concurrent web scraper to identify all bugs:

1. **Main Bug - Sequential Execution**: The `t.join()` call is inside the loop, which means each thread is started and then immediately joined before starting the next one. This defeats the purpose of threading and m...
```

---

### Data Analysis Report

- **Time**: 3.72s
- **Speed**: 161.3 tok/s
- **TTFT (est.)**: 0.372s

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
- **Speed**: 168.7 tok/s
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

- **Time**: 4.75s
- **Speed**: 168.4 tok/s
- **TTFT (est.)**: 0.475s

**Response Preview:**
```
Thinking Process:

1.  **Analyze the Request:**
    *   **Role:** Senior Software Engineer.
    *   **Task:** Continue a debugging conversation about a slow Python app in production.
    *   **Context:** The user has a Python app, slow response times (2-5s for simple queries), 1M+ row table, indexes...
```

---

### Technical Documentation

- **Time**: 4.15s
- **Speed**: 168.6 tok/s
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

- **Time**: 2.98s
- **Speed**: 167.5 tok/s
- **TTFT (est.)**: 0.298s

**Response Preview:**
```
This is a comprehensive database optimization question. Let me analyze the query and provide detailed recommendations.

1. **Performance Issues to Identify:**
   - Subquery in IN clause may cause performance issues
   - SELECT * retrieves unnecessary data
   - Missing indexes on key columns
   - Pot...
```

---

### ML Project

- **Time**: 4.75s
- **Speed**: 168.6 tok/s
- **TTFT (est.)**: 0.475s

**Response Preview:**
```
This is a comprehensive request for building a complete ML pipeline for customer churn prediction. I need to create a production-ready codebase that covers all 8 requirements. Let me structure this properly:

1. **Exploratory Data Analysis (EDA)** - Understanding the data distribution, correlations,...
```

---


## Conclusion

**Performance Rating**: Excellent

- Average Speed: 153.1 tok/s

---
*Generated by benchmark script*
