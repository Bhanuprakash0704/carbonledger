from django.db import models


class Tenant(models.Model):

    company_name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


class Source(models.Model):

    SOURCE_TYPES = [
        ('sap', 'SAP'),
        ('utility', 'Utility'),
        ('travel', 'Travel'),
    ]

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_TYPES
    )

    file_name = models.CharField(max_length=255)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name


class EmissionRecord(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('locked', 'Locked'),
    ]

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    source = models.ForeignKey(
        Source,
        on_delete=models.CASCADE
    )

    category = models.CharField(max_length=100)

    scope = models.IntegerField()

    quantity = models.FloatField()

    unit = models.CharField(max_length=20)

    normalized_quantity = models.FloatField(
        null=True,
        blank=True
    )

    normalized_unit = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    co2e = models.FloatField(
        null=True,
        blank=True
    )

    suspicious = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    raw_data = models.JSONField(
        null=True,
        blank=True
    )

    edited_by_analyst = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.category} - {self.quantity} {self.unit}"