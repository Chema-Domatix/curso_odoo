# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association",
    "summary": "Manage sports associations members, teams and events",
    "version": "17.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    "category": "Sports",
    "author": "<Chema Fernández>, Domatix",
    # see https://odoo-community.org/page/maintainer-role for a description of the maintainer role and responsibilities
    "maintainers": ["your-github-login"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
    ],
    
    "data": [
            "security/groups.xml",
            "security/ir.model.access.csv",
             "views/sport_issue.xml",
             "views/sport_issue_views.xml",
             "views/sport_clinic_views.xml"
             ],
}