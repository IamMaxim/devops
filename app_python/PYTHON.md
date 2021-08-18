# Lab Report
> DevOps Lab 1
> <br>
> Maxim Stepanov, BS18-SE-01

---

# 1. Web application

## 1. AWS account
I have already registered an Amazon Web Services account during the previous course, so I skipped this step.

## 2. Python Web Application
I decided to pick Django for the app. It may be an overkill, but this is the framework I currently use in my work project, so I feel comfortable with it.

As for linters: I use PyCharm, and it has built-in linters for literally everything (Python and Markdown included). Default settings are quite fine, I didn't change them.

As for the best practices:
 - It is always a good idea to create a reproducible environment. So, I used `requirements.txt` file to specify all Python dependencies (including particular versions!). It will also be used later to containerize the app.
 - Django is a prod ready framework :) It has a rich ecosystem of plugins and huge community. But if I was picking a framework for the next project, I would go for something else. Python developers do not often think about the project structure and code cleanness, as a result many of built-in Django parts and external plugins do not work well together or even contradict each other. For me, it is a huge PITA in a large project. This PoC app is perfectly suitable for Django, though.
 - Creating unresponsive web apps is not considered good, especially for a time-showing app :) Thus, I added server polling to update time without refreshing page.
 - Initial load time is crucial for the web, so I still include server-side rendering of initial content. The initial time is embedded in the page, so it is immediately available to the web client after HTML load.
 - Carrying heavy DBMS around with no actual data sounds ridiculous to me. So I used \*lightweight\* SQLite (SQL DBMS is required for Django to store the basic information about project environment, so it is not possible to get rid of it completely).
 - Time is returned in ISO format, so both humans and crawlers may universally read/parse it.

## 