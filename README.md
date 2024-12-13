# Blog Documentation on Flask

## Project Description

This project is a blog developed using Flask. It allows users to view posts, add new entries, and leave comments.

## Project Structure

```
myblog/
├── instance/
│   ├── __init__.py
│   └── config.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── post.html
│   └── new_post.html
├── app.py
├── requirements.txt
└── README.md
```

### Directory and File Descriptions

- `instance/`: Configuration files.
  - `__init__.py`: Package initialization.
  - `config.py`: Application configuration.
  
- `templates/`: HTML templates.
  - `base.html`: Common page structure.
  - `index.html`: Home page.
  - `post.html`: Post page.
  - `new_post.html`: New post page.
  
- `app.py`: Main application file.
  
- `requirements.txt`: Project dependencies.

## Installation and Running the Project

### Prerequisites

- Python 3.8+
- pip

### Cloning the Repository

```bash
git clone https://github.com/AlexTkDev/MyFlaskProject.git
cd myblog
```

### Installing Dependencies

```bash
pip install -r requirements.txt
```

### Running the Application

```bash
flask run
```

The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Using Bootstrap 5

Bootstrap 5 is used for styling the pages, included through `base.html`.

## Application Routes

### Home Page

Route: `/`

Description: Displays all posts.

### Post Page

Route: `/post/<post_id>`

Description: Displays the selected post.

### New Post

Route: `/new`

Description: Form for adding a new post.

## Conclusion

This project is a simple blog on Flask that can be extended and modified to suit your needs. Flask provides flexibility and ease of development, and using templates and Bootstrap 5 allows for creating modern and responsive interfaces.

