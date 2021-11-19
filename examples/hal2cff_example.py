from hal2cff import hal2cff
# # hal2cff example

import ipywidgets as widgets
from IPython.display import display, display_html, Markdown

example_query = "https://hal.archives-ouvertes.fr/hal-01361430v1"

query = widgets.Textarea(value=example_query)
button = widgets.Button(description="Run query")
display(widgets.HBox([query, button]))
output = widgets.Output()
display(output)

def run_and_display_query(_):
    result = hal2cff(query.value)
    with output:
        output.clear_output()
        display_html("<pre>{}</pre>".format(result), raw=True)

button.on_click(run_and_display_query)


