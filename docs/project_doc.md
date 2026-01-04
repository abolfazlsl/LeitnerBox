# Leitner Box Learning System

## 1. Project Overview
This project implements a learning system based on the **Leitner Box** method, allowing users to create educational flashcards and review them based on the Leitner algorithm.
The system uses **PostgreSQL** for data storage, with a relational and normalized database design.

## 2. Objectives
- Design a standard and normalized database.
- Support multiple users.
- Implement Leitner Box logic.
- Manage card review timing.
- Store review history for progress analysis.

## 3. Technology Stack
| Section | Technology |
| :--- | :--- |
| **Database** | PostgreSQL |
| **Design** | DBML (dbdiagram.io) |
| **Language** | Python |
| **Architecture** | OOP |
| **Environment** | venv |
| **Config** | .env |

## 4. Database Design
### Main Tables:
- `users`
- `slots`
- `cards`
- `card_reviews`

### Relationships:
- Each user has multiple cards.
- Each card is placed in a Slot.
- Each card can be reviewed multiple times.

## 5. Business Logic (Leitner Box)
- Cards initially start in **Slot 1**.
- **Correct Answer** → Move to the next Slot.
- **Wrong Answer** → Return to previous Slot (or Slot 1, depending on specific rule, usually Slot 1 in strict Leitner, but prompt says "Return to previous Slot").
  - *Correction based on prompt*: "ba pasokh ghalat -> bazgasht be Slot ghabli" (Return to previous Slot).
- Slots have time intervals for review.
- If a card review is delayed by more than **2 days** → The card is downgraded (demoted).

## 6. Team Roadmap
### 👤 Member 1 — Team Leader (Abolfazl)
**Responsibilities:**
- Database Design (DBML + ERD)
- Define Project Structure
- Define Leitner Logic
- Team Coordination
- Final Review and Integration

**Deliverables:**
- DBML Schema
- ERD Diagram
- Project Documentation
- Final Code Review

### 👤 Member 2 — Database & Logic Developer (Naser)
**Responsibilities:**
- Implement PostgreSQL Database
- Create Tables
- Write Main Queries
- Test Card Review Logic

**Deliverables:**
- SQL Scripts
- Test Data
- Query Examples

### 👤 Member 3 — Application Developer (Alireza)
**Responsibilities:**
- Implement Python Application
- CRUD for Cards
- Record Reviews
- Calculate `next_review_at`

**Deliverables:**
- Python Source Code
- CLI Interface
- Test Scenarios

