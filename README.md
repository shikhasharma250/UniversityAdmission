# University Admission System

A Python program that automates the university admission process by validating student data and checking qualification based on exam marks and age.

---

## Problem Statement

A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exam.

---

##  Validation Rules

| Field | Rule |
|-------|------|
| Age   | Must be **greater than 20** |
| Marks | Must be **between 0 and 100** (inclusive) |

##  Qualification Criteria

A student qualifies for admission if:
- Age and marks are **valid**, AND
- Marks are **65 or above**

---

##  Class Structure

### `Student`

| Member | Type | Description |
|--------|------|-------------|
| `__name` | Private | Name of the student |
| `__student_id` | Private | Unique student identifier |
| `__marks` | Private | Marks scored in qualifying exam |
| `__age` | Private | Age of the student |

### Methods

| Method | Description |
|--------|-------------|
| `get__marks()` | Returns the student's marks |
| `set__marks(new_marks)` | Sets marks if valid numeric value |
| `validate_marks()` | Returns `True` if marks are between 0–100 |
| `validate_age()` | Returns `True` if age is greater than 20 |
| `check_qualification()` | Prints qualification status |

---

##  Usage

```python
S1 = Student("Shikha", 101, 70, 20)
S1.check_qualification()   # Not qualified (age not > 20)

S2 = Student("Suniti", 102, 80, 21)
S2.check_qualification()   # Qualified

S3 = Student("Tanish", 103, "hehe", 20)
S3.check_qualification()   # Invalid data
```

### Output

```
Shikha: Not qualified
Suniti: Qualified
Tanish: Invalid data
```




