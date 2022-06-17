import os, json
import jinja2 as jj, markdown2 as md2

template_env = jj.Environment(loader=jj.FileSystemLoader(searchpath='./'))
template = template_env.get_template('static/layout.html')
css_paths = ["../gen/static/styles.css", "../gen/static/bootstrap.css"]
js_paths = ["//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js", 
            "https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"]

with open('json/config.json') as f:  # get art_cfgs
    art_cfgs = json.load(f)
    n_arts = len(art_cfgs)

def checks():
    name_list = {cfg["md_filename"] for cfg in art_cfgs}
    file_list = {s.replace('.md', '') for s in os.listdir("md")}
    file_list = {s for s in file_list if s[0] != '.'}
    test = name_list == file_list
    if not test:
        print(name_list)
        print(file_list)
        quit()
checks()

for cfg in art_cfgs:
    name = cfg["md_filename"]
    with open(f"md/{name}.md") as f:
        art_html = md2.markdown(f.read())
    
    path = f"../pages/{name}.html"
    with open(path, 'w') as f:
        f.write(
            template.render(
                art_cfgs=art_cfgs,
                n_arts=n_arts,
                cfg=cfg,
                art_html=art_html,
                css_paths=css_paths,
                js_paths=js_paths
            )
        )


 
