from clients.auth_client import AuthClient
from clients.payment_client import PaymentClient
from clients.storage_client import StorageClient
from clients.notify_client import NotifyClient
from clients.gateway_client import GatewayClient


class DashboardService:

    def __init__(self):

        self.auth = AuthClient()

        self.payment = PaymentClient()

        self.storage = StorageClient()

        self.notify = NotifyClient()

        self.gateway = GatewayClient()

    def overview(self):

        return {

            "auth": self.auth.summary(),

            "payment": self.payment.summary(),

            "storage": self.storage.summary(),

            "notify": self.notify.summary(),

            "gateway": self.gateway.summary()

        }
