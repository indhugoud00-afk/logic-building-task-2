#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1(Unique words in a sentence)


# In[2]:


sentence = "python is easy and python is powerful"
words = sentence.split()
unique_words = set(words)
print(f"Unique words count: {len(unique_words)}")
print(f"Unique words: {unique_words}")


# 2(highest salary from employee data)

# In[3]:


employees = {"Ravi": 75000, "Anita": 68000, "Kiran": 72000}
highest_paid = max(employees, key=employees.get)
print(f"Highest Salary: {highest_paid} - {employees[highest_paid]}")


# In[ ]:


3(find max and min)


# In[5]:


numbers = [45, 22, 89, 10, 66]
max = numbers[0]
min = numbers[0]
for num in numbers:
    if num > max: max = num
    if num < min: min = num
print(f"List: {numbers}")
print(f"Max: {max}")
print(f"Min: {min}")


# In[ ]:


4(count products above a price threshold)


# In[6]:


prices = [450, 1200, 899, 1500, 300]
count = 0
for price in prices:
    if price > 1000:
        count+=1
print(f"Products above 1000: {count}")


# In[ ]:


5(calculate attendance percentage)


# In[11]:


attendance = ["P", "P", "A", "P", "P"]
present_count = attendance.count("P")
percentage = (present_count / len(attendance)) * 100
print(f"Attendance Percentage: {percentage}")


# In[ ]:


6(remove duplicate phone numbers)


# In[9]:


phone_numbers = [9876543210, 9123456789, 9876543210]
unique_numbers= set(phone_numbers)
print(f"Unique phone numbers: {unique_numbers}")


# In[ ]:


7(count character frequency)


# In[16]:


text = "pythonP"
freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)


# In[ ]:


8(convert list to tuple)


# In[17]:


data_list = [10,20,30]
data_tuple = tuple(data_list)
print(f"Tuple: {data_tuple}")


# In[ ]:


9(check if a key exists in a dictionary)


# In[18]:


employees = {"Ravi": 75000, "Anita":68000}
if "Ravi" in employees:
    print("Employee exists")


# In[ ]:


10(calculate avg marks)


# In[19]:


marks = [80, 70, 60, 80]
average = sum(marks) / len(marks)
print(f"Average Marks: {average}")


# In[ ]:




