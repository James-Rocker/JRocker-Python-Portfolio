from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.datafactory import DataFactoryManagementClient


def print_item(group):
    """Print an Azure object instance."""
    print("\tName: {}".format(group.name))
    print("\tId: {}".format(group.id))
    if hasattr(group, "location"):
        print("\tLocation: {}".format(group.location))
    if hasattr(group, "tags"):
        print("\tTags: {}".format(group.tags))
    if hasattr(group, "properties"):
        print_properties(group.properties)


def print_properties(props):
    """Print a ResourceGroup properties instance."""
    if props and hasattr(props, "provisioning_state") and props.provisioning_state:
        print("\tProperties:")
        print("\t\tProvisioning State: {}".format(props.provisioning_state))
    print("\n\n")


def print_activity_run_details(activity_run):
    """Print activity run details."""
    print("\n\tActivity run details\n")
    print("\tActivity run status: {}".format(activity_run.status))
    if activity_run.status == "Succeeded":
        print("\tNumber of bytes read: {}".format(activity_run.output["dataRead"]))
        print(
            "\tNumber of bytes written: {}".format(activity_run.output["dataWritten"])
        )
        print("\tCopy duration: {}".format(activity_run.output["copyDuration"]))
    else:
        print("\tErrors: {}".format(activity_run.error["message"]))


if __name__ == "__main__":

    def main():
        # Azure subscription ID
        subscription_id = "<Specify your Azure Subscription ID>"

        # This program creates this resource group.
        rg_name = "ADFTutorialResourceGroup"

        # The data factory name. It must be globally unique.
        df_name = "<Specify a name for the data factory. It must be globally unique>"

        # Specify your Active Directory client ID, client secret, and tenant ID
        credentials = ServicePrincipalCredentials(
            client_id="<Active Directory application/client ID>",
            secret="<client secret>",
            tenant="<Active Directory tenant ID>",
        )
        resource_client = ResourceManagementClient(credentials, subscription_id)
        adf_client = DataFactoryManagementClient(credentials, subscription_id)

        rg_params = {"location": "eastus"}
        df_params = {"location": "eastus"}
