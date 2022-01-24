
import jinja2


def main():
    context = {
        'pool_name': "PHY"
    }
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates')
    )
    yaml = env.get_template('azure-pipelines.yaml.template')

    rendered = yaml.render(context)
    print(rendered)

    with open('templates/azure-pipelines.yaml.template', 'w') as f:
        f.write(rendered)
    

if __name__ == "__main__":
    main()