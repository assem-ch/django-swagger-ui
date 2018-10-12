import json
import yaml
from django.shortcuts import render
from swagger_viewer.settings import SWAGGER_YAML_FILE


def yaml_to_html(request):
    file = open(SWAGGER_YAML_FILE)
    spec = yaml.load(file.read())
    return render(request, template_name="swagger_base.html", context={'data': json.dumps(spec)})
