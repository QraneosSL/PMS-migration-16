from freezegun import freeze_time

from odoo.tests.common import TransactionCase

freeze_time("2000-02-02")


class TestPmsInvoiceRefund(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
