# Website Generator

This Python script implements a website generator using the Composite design pattern. The generator allows the creation of various types of websites (such as portfolio, business, or personal blog) by combining different components in a specific order and combination

## Components

The script defines several components that can be used to build a website:


- **HomePage**: Represents the homepage of the website.
- **AboutPage**: Represents the about page of the website.
- **ContactForm**: Represents a contact form for the website.
- **Gallery**: Represents a gallery section for the website.
- **Blog**: Represents a blog section for the website.

Additionally, it provides two new leaf components:

- **ServicesPage**: Represents a services page for the website.
- **Footer**: Represents a footer section for the website.

- ## Composite Component

The Website class serves as a composite component, allowing the combination of various components to form a complete website. It contains methods to add and remove components, as well as a render method to generate the HTML code for the entire website.

## Usage
To use the website generator, simply create instances of the desired components and add them to a Website object. The order in which components are added determines the structure of the resulting website. Finally, call the render method on the Website object to obtain the HTML code for the generated website.

Example usage:

```python
from website_generator import HomePage, AboutPage, ContactForm, Gallery, Blog, Website

home_page = HomePage()
about_page = AboutPage()
contact_form = ContactForm()
gallery = Gallery()
blog = Blog()

website = Website()
website.add_component(home_page)
website.add_component(about_page)
website.add_component(contact_form)
website.add_component(gallery)
website.add_component(blog)

print(website.render())
