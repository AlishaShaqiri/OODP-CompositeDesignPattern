from website_generator import HomePage, AboutPage, ContactForm, Gallery, Blog, Website

if __name__ == "__main__":
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