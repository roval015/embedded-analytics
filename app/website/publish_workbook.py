
# This was supposed to be for publishing the workbook but we were not able to complete it as we do not have a proper tableau server set up
# Reference: https://youtu.be/swasTFYM_Gs

from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils import querying

config = {
    'tableau_server': {
        'server': '',
        'api_version': '',
        'personal_access_token_name': '',
        'personal_access_token_secret': '',
        'site_name': '',
        'site_url': ''
    }
}

conn = TableauServerConnection(config, env="tableau_server")
conn.sign_in()

projects_df = querying.get_projects_dataframe(conn)

project_id = ""

response = conn.publish_workbook(
    project_id = project_id,
    workbook_file_path= "",
    workbook_name= ""
)