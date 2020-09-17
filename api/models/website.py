import base64
import uuid
import string
import random

from django.db import models


def generate_hidden_domain(domain_len=10):
    """
    Generate the random hidden domain for a website
    """
    return base64.b32encode(uuid.uuid4().bytes)[:domain_len].lower()


def generate_ats_purge_secret():
    """
    Generate the random ATS purge secret for a website
    """
    return ''.join(random.choice(
        string.ascii_lowercase + string.ascii_uppercase) for _ in range(16))


class Website(models.Model):
    """
    Model of website
    """
    class Meta:
        app_label = "api"

    id = models.AutoField(primary_key=True)

    # url = db.Column(db.String(255), unique=True, nullable=False)
    url = models.CharField(max_length=10, unique=True, null=False)

    # status = db.Column(db.Float, default=0, nullable=False)
    status = models.FloatField(default=0, null=False)

    # ip_address = db.Column(db.String(16))
    ip_address = models.CharField(max_length=16)

    # hidden_domain = db.Column(db.String(32), nullable=False, default=generate_hidden_domain)
    hidden_domain = models.CharField(max_length=32, null=False, default=generate_hidden_domain)

    # banjax_auth_hash = db.Column(db.String(255))
    banjax_auth_hash = models.CharField(max_length=255, null=False, default='')

    # admin_key = db.Column(db.String(255))
    admin_key = models.CharField(max_length=255, null=False, default='')

    # under_attack = db.Column(db.Integer, default=0)
    under_attack = models.BooleanField(default=False)

    # awstats_password = db.Column(db.String(40), nullable=False, default=lambda: uuid.uuid4())
    awstats_password = models.CharField(max_length=40, null=False, default=uuid.uuid4())

    # ats_purge_secret = \
    #     db.Column(db.String(64), default=lambda: ''.join(
    #         random.choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(16)))
    ats_purge_secret = models.CharField(max_length=64, default=generate_ats_purge_secret)

    # created = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True)
