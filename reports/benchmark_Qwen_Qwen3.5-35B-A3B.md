# Qwen/Qwen3.5-35B-A3B Performance Benchmark Report

## Test Information

- **Test Time**: 2026-02-28 15:59:26
- **Model**: Qwen/Qwen3.5-35B-A3B
- **API URL**: http://localhost:30000/v1/chat/completions
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
| **Avg Generation Speed** | **165.7 tok/s** |
| Total Time | 39.81s |
| Total Tokens | 6600 |

### Speed Statistics

- **Max**: 168.7 tok/s
- **Min**: 159.0 tok/s
- **Median**: 166.3 tok/s

## Detailed Results

| Test Case | Time | Prompt | Completion | Speed |
|-----------|------|--------|------------|-------|
| Full Backend System | 4.87s | 92 | 800 | **164.4** tok/s |
| Microservices Architecture | 3.77s | 101 | 600 | **159.0** tok/s |
| Complex Algorithms | 4.19s | 56 | 700 | **167.0** tok/s |
| Debug Task | 3.03s | 166 | 500 | **165.1** tok/s |
| Data Analysis Report | 3.61s | 112 | 600 | **166.2** tok/s |
| System Design Interview | 3.56s | 92 | 600 | **168.7** tok/s |
| Multi-turn Conversation | 4.81s | 142 | 800 | **166.3** tok/s |
| Technical Documentation | 4.19s | 88 | 700 | **167.1** tok/s |
| Database Optimization | 3.02s | 133 | 500 | **165.3** tok/s |
| ML Project | 4.77s | 142 | 800 | **167.8** tok/s |

## Test Details

### Full Backend System

- **Time**: 4.87s
- **Speed**: 164.4 tok/s
- **TTFT (est.)**: 0.487s

**Response Preview:**
```
This is a comprehensive request that requires creating a complete FastAPI REST API with authentication, database operations, testing, and deployment configuration. I'll need to create:

1. Project structure
2. Main FastAPI application
3. Database models (SQLAlchemy)
4. Pydantic schemas
5. Authentica...
```

---

### Microservices Architecture

- **Time**: 3.77s
- **Speed**: 159.0 tok/s
- **TTFT (est.)**: 0.377s

**Response Preview:**
```
Here's a thinking process that leads to the suggested microservices architecture:

1.  **Understand the Goal:** The user wants a detailed technical design for a microservices architecture specifically for an e-commerce platform. The design needs to cover seven specific areas: Service breakdown, API ...
```

---

### Complex Algorithms

- **Time**: 4.19s
- **Speed**: 167.0 tok/s
- **TTFT (est.)**: 0.419s

**Response Preview:**
```
This is a comprehensive request that requires me to:
1. Implement A* pathfinding algorithm
2. Implement Dijkstra's algorithm
3. Compare their time complexity
4. Include visualization examples
5. Include test cases

Let me create a complete, well-documented solution with:
- Clear class structures
- D...
```

---

### Debug Task

- **Time**: 3.03s
- **Speed**: 165.1 tok/s
- **TTFT (est.)**: 0.303s

**Response Preview:**
```
Let me analyze this Python code for a concurrent web scraper. I can identify several issues:

1. **Major Bug - Sequential Execution**: The `t.join()` is inside the loop, which means each thread is joined immediately after it's started. This defeats the purpose of threading and makes the code execute...
```

---

### Data Analysis Report

- **Time**: 3.61s
- **Speed**: 166.2 tok/s
- **TTFT (est.)**: 0.361s

**Response Preview:**
```
This is a comprehensive request for retail sales data analysis. I need to create a complete Python pipeline that covers all 6 tasks mentioned. Let me structure this properly:

1. First, I'll need to create a sample dataset structure since no actual data is provided
2. Data cleaning and preprocessing...
```

---

### System Design Interview

- **Time**: 3.56s
- **Speed**: 168.7 tok/s
- **TTFT (est.)**: 0.356s

**Response Preview:**
```
Here's a thinking process that leads to the suggested design for a URL shortening service:

1.  **Understand the Goal:** The objective is to design a URL shortening service (like bit.ly) covering specific technical aspects: API endpoints, DB schema, hash function, rate limiting, caching, analytics, ...
```

---

### Multi-turn Conversation

- **Time**: 4.81s
- **Speed**: 166.3 tok/s
- **TTFT (est.)**: 0.481s

**Response Preview:**
```
Thinking Process:

1.  **Analyze the Request:**
    *   **Role:** Senior Software Engineer.
    *   **Task:** Continue a debugging conversation about a slow Python app (2-5 seconds for simple SELECT queries on 1M+ rows, indexes not being used).
    *   **Constraint:** At least 5 more exchanges (User...
```

---

### Technical Documentation

- **Time**: 4.19s
- **Speed**: 167.1 tok/s
- **TTFT (est.)**: 0.419s

**Response Preview:**
```
Here's a thinking process that leads to the suggested documentation:

1.  **Understand the Goal:** The user wants comprehensive documentation for a Python CLI tool. The tool's core functionalities are image compression (PNG, JPEG, WebP), batch processing, quality control, and statistics output. The ...
```

---

### Database Optimization

- **Time**: 3.02s
- **Speed**: 165.3 tok/s
- **TTFT (est.)**: 0.302s

**Response Preview:**
```
This is a comprehensive PostgreSQL performance optimization question. Let me analyze each aspect systematically:

1. **Performance Issues:**
   - Subquery in WHERE clause (IN with subquery)
   - SELECT * (selecting all columns when not needed)
   - Multiple filters without proper indexes
   - ORDER ...
```

---

### ML Project

- **Time**: 4.77s
- **Speed**: 167.8 tok/s
- **TTFT (est.)**: 0.477s

**Response Preview:**
```
Here's a thinking process that leads to the suggested ML pipeline for customer churn prediction:

1.  **Understand the Goal:** The user wants a *complete* Machine Learning pipeline for predicting customer churn. The dataset is described as having 50 features (demographics, account info, usage patter...
```

---


## Conclusion

**Performance Rating**: Excellent

- Average Speed: 165.7 tok/s

---
*Generated by benchmark script*
