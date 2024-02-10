from abc import ABC, abstractmethod

class WebsiteComponent(ABC):
    @abstractmethod
    def render(self):
        pass

class HomePage(WebsiteComponent):
    def render(self):
        return "<div class='homepage'>Rendered Home Page</div>"

class AboutPage(WebsiteComponent):
    def render(self):
        return "<div class='aboutpage'>Rendered About Page</div>"

class ContactForm(WebsiteComponent):
    def render(self):
        return "<div class='contactform'>Rendered Contact Form</div>"

class Gallery(WebsiteComponent):
    def render(self):
        return "<div class='gallery'>Rendered Gallery</div>"

class Blog(WebsiteComponent):
    def render(self):
        return "<div class='blog'>Rendered Blog</div>"

class ServicesPage(WebsiteComponent):
    def render(self):
        return "<div class='servicespage'>Rendered Services Page</div>"

class Footer(WebsiteComponent):
    def render(self):
        return "<div class='footer'>Rendered Footer</div>"

class Website(WebsiteComponent):
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def render(self):
        result = ""
        for component in self.components:
            result += component.render() + "\n"
        return result