from smtplib import SMTP_SSL
from ssl import create_default_context
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .models import Restaurant

default_context = create_default_context()
def send_email_for(restaurant_ids, session):
    restaurants = session.query(Restaurant.name,
                                Restaurant.open_hours,
                                Restaurant.image_url).filter(
        Restaurant.identifier_id.in_(restaurant_ids)).all()

    pswd = getpass()
    with SMTP_SSL('smtp.gmail.com', context=default_context) as smtp_server:
        smtp_server.login('programmingangela@gmail.com', pswd)

        restaurant_text = "\n".join(f"{name}-{open_hours}" for name, open_hours, _ in restaurants)
        text_content = f"""
        Hi, 
        Check out new Restaurants from BuyAm:
        {restaurant_text}
        Have a nice day!
        """

        restaurant_html_div_list = []
        for name, open_hours, image_url in restaurants:
            html = f"""
            <div><img src={image_url} alt="img" />{name}-{open_hours}</div>" 
            """
            restaurant_html_div_list.append(html)
        restaurant_html = '\n'.join(restaurant_html_div_list)
        html_content = f"""
        <h2>Hi</h2>
        <p>Check out new Restaurants from BuyAm:</p>
        {restaurant_html}
        <p>Have a nice day!</p>
        """
        message = MIMEMultipart('altrnative')
        message['Subject'] = 'Testing'
        message['To'] = 'programmingangela@gmail.com'
        text = MIMEText(text_content, 'plane')
        html = MIMEText(html_content, 'html')
        message.attach(html)
        message.attach(text)
        smtp_server.sendmail('programmingangela@gmail.com', 'programmingangela@gmail.com',
                             msg=message.as_string())


