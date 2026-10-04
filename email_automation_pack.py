# Reusable Email Automation Package
# This module contains the ReplyTemplateLibrary to manage and render brand-consistent responses.

class ReplyTemplateLibrary:
    def __init__(self):
        self.templates = {}
        self._load_default_templates()

    def _load_default_templates(self):
        self.add_template('Cancellation',
            "Hi {name},

Thank you for reaching out. We have successfully processed your request to cancel your subscription/membership. "
            "While we are sad to see you go, we hope to serve you again in the future.

Best regards,
{sender_team}"
        )
        self.add_template('Bulk/B2B order',
            "Hi {name},

Thank you for your interest in our wholesale opportunities! "
            "One of our B2B representatives will reach out to you within 24 business hours to assist you with pricing and details.

Warm regards,
{sender_team}"
        )
        self.add_template('Complaint',
            "Hi {name},

We are incredibly sorry to hear about your experience. This is not the standard we strive for. "
            "Our team has been notified, and we are looking into resolving this for you immediately.

Sincerely,
{sender_team}"
        )
        self.add_template('Appreciation',
            "Hi {name},

Thank you so much for taking the time to share your kind words with us! "
            "We are thrilled to hear about your positive experience.

Warmly,
{sender_team}"
        )
        self.add_template('Product inquiry',
            "Hi {name},

Thanks for asking! We appreciate your interest in our products. "
            "Our specialists are compiling the information you requested and will get back to you shortly.

Best regards,
{sender_team}"
        )
        self.add_template('Partnership',
            "Hi {name},

Thank you for reaching out regarding a potential collaboration! "
            "We have shared your proposal with our partnerships team for review.

Best regards,
{sender_team}"
        )
        self.add_template('Refund request',
            "Hi {name},

We have received your refund request. "
            "Our billing department is currently processing this transaction, and you should see the credit reflected in 3-5 business days.

Best regards,
{sender_team}"
        )

    def add_template(self, intent, template_text):
        self.templates[intent] = template_text

    def get_template(self, intent):
        return self.templates.get(intent, "Hi {name},

Thank you for reaching out. We are processing your request.

Best regards,
{sender_team}")

    def render(self, intent, **kwargs):
        template = self.get_template(intent)
        kwargs.setdefault('name', 'Customer')
        kwargs.setdefault('sender_team', 'Customer Support Team')
        try:
            return template.format(**kwargs)
        except KeyError as e:
            return template
