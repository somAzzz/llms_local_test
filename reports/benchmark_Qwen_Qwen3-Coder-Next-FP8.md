# Qwen/Qwen3-Coder-Next-FP8 Performance Benchmark Report

## Test Information

- **Test Time**: 2026-02-19 17:35:44
- **Model**: Qwen/Qwen3-Coder-Next-FP8
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
| **Avg Generation Speed** | **147.5 tok/s** |
| Total Time | 44.73s |
| Total Tokens | 6600 |

### Speed Statistics

- **Max**: 147.8 tok/s
- **Min**: 147.1 tok/s
- **Median**: 147.6 tok/s

## Detailed Results

| Test Case | Time | Prompt | Completion | Speed |
|-----------|------|--------|------------|-------|
| Full Backend System | 5.42s | 88 | 800 | **147.6** tok/s |
| Microservices Architecture | 4.06s | 95 | 600 | **147.7** tok/s |
| Complex Algorithms | 4.73s | 53 | 700 | **147.8** tok/s |
| Debug Task | 3.40s | 148 | 500 | **147.1** tok/s |
| Data Analysis Report | 4.07s | 107 | 600 | **147.6** tok/s |
| System Design Interview | 4.06s | 86 | 600 | **147.7** tok/s |
| Multi-turn Conversation | 5.42s | 135 | 800 | **147.5** tok/s |
| Technical Documentation | 4.74s | 84 | 700 | **147.5** tok/s |
| Database Optimization | 3.40s | 125 | 500 | **147.1** tok/s |
| ML Project | 5.42s | 133 | 800 | **147.6** tok/s |

## Test Details

### Full Backend System

- **Time**: 5.42s
- **Speed**: 147.6 tok/s
- **TTFT (est.)**: 0.542s

**Response Preview:**
```
Here's a complete, production-ready Python REST API using FastAPI with all requested features. I'll provide the full file structure and code.

---

## 📁 Project Structure

```
fastapi-blog-api/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app entry point
│   ├── config.py  ...
```

---

### Microservices Architecture

- **Time**: 4.06s
- **Speed**: 147.7 tok/s
- **TTFT (est.)**: 0.406s

**Response Preview:**
```
Here's a comprehensive, production-grade microservices architecture for an e-commerce platform, designed for scalability, resilience, and maintainability.

---

## **1. Service Breakdown & Technical Specifications**

| Service | Responsibility | Key APIs | Tech Stack | Database |
|---------|--------...
```

---

### Complex Algorithms

- **Time**: 4.73s
- **Speed**: 147.8 tok/s
- **TTFT (est.)**: 0.473s

**Response Preview:**
```
# A* and Dijkstra's Algorithms: Comprehensive Guide

Below is a detailed implementation of both algorithms with thorough comments, complexity analysis, and visualization examples.

```python
import heapq
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as...
```

---

### Debug Task

- **Time**: 3.40s
- **Speed**: 147.1 tok/s
- **TTFT (est.)**: 0.340s

**Response Preview:**
```
Looking at this code, there are several issues that need to be addressed:

## Bugs Identified:

1. **Main Bug**: `t.join()` inside the loop (line 17) - This causes threads to run sequentially instead of concurrently. Each thread is started and immediately joined, so the next thread doesn't start unt...
```

---

### Data Analysis Report

- **Time**: 4.07s
- **Speed**: 147.6 tok/s
- **TTFT (est.)**: 0.407s

**Response Preview:**
```
Here's a **complete, production-ready Python analysis pipeline** for your retail sales dataset. This pipeline covers all requested tasks with best practices, modular design, and clear documentation.

---

### 📦 Assumptions about the Dataset Structure
We assume the dataset is in a CSV file (`retail_s...
```

---

### System Design Interview

- **Time**: 4.06s
- **Speed**: 147.7 tok/s
- **TTFT (est.)**: 0.406s

**Response Preview:**
```
Here's a comprehensive, production-grade design for a scalable URL shortening service (e.g., "BitlyClone") covering all requested aspects with implementation details.

---

### **1. RESTful API Endpoints**

**Base URL**: `https://api.example.com/v1`

| Method | Endpoint | Description | Request Body ...
```

---

### Multi-turn Conversation

- **Time**: 5.42s
- **Speed**: 147.5 tok/s
- **TTFT (est.)**: 0.542s

**Response Preview:**
```
**Assistant:** Great—let’s dig into the `EXPLAIN` output. Can you share the full `EXPLAIN (ANALYZE, BUFFERS)` output for one of those slow queries? Also, what does your table schema look like (especially the indexed columns and the `WHERE` clause you’re using)? Without seeing the actual plan, we’re ...
```

---

### Technical Documentation

- **Time**: 4.74s
- **Speed**: 147.5 tok/s
- **TTFT (est.)**: 0.474s

**Response Preview:**
```
# **Imagix: Advanced Image Compression CLI Tool**

---

## 📦 Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage Guide](#usage-guide)
   - [Basic Usage](#basic-usage)
   - [Batch Processing](#batch-processing)
   - [Quality Control](#quality-control)
   - [Statistic...
```

---

### Database Optimization

- **Time**: 3.40s
- **Speed**: 147.1 tok/s
- **TTFT (est.)**: 0.340s

**Response Preview:**
```
Let's analyze and optimize this PostgreSQL query systematically.

---

### **1. Performance Issues**

| Issue | Explanation |
|-------|-------------|
| **Subquery with IN clause** | The `IN (subquery)` forces PostgreSQL to materialize the subquery result and then perform a hash join or nested loop —...
```

---

### ML Project

- **Time**: 5.42s
- **Speed**: 147.6 tok/s
- **TTFT (est.)**: 0.542s

**Response Preview:**
```
Here's a complete, production-ready ML pipeline for customer churn prediction using Python. This implementation uses `scikit-learn`, `imbalanced-learn`, `xgboost`, `shap`, and follows best practices.

---

### ✅ **Complete Churn Prediction Pipeline**

```python
# ====================================...
```

---


## Conclusion

**Performance Rating**: Excellent

- Average Speed: 147.5 tok/s

---
*Generated by benchmark script*
