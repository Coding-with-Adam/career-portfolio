# These first 3 lines of code are needed when running the app in https://wasmdash.vercel.app/
# import micropip
# await micropip.install('dash-mantine-components')
# await micropip.install('dash-iconify')
import dash_mantine_components as dmc
from dash import Dash, html, dcc
from dash_iconify import DashIconify

card1 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.im.ge/2024/01/11/3xIdOh.your-project-filler-1.png",
                    alt="American Football Oracle GPT",
                ),
                href="https://chat.openai.com/g/g-RWX3i8Zfr-american-football-oracle",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("American Football Oracle", weight=500, size='xl'),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/Coding-with-Adam/Dash-by-Plotly/tree/master/AI/Create-Your-Own-GPT',
                    target="_blank"
                )
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "An NFL GPT to analyze team performance, strategies, and game predictions.",
            size="sm",
            color="dimmed",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

card2 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.im.ge/2024/01/11/3xI4b4.investment-app.png",
                    alt="dash-app",
                ),
                href="https://investment-app.onrender.com/",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Investment Portfolio", weight=500, size='xl'),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/Coding-with-Adam/investing-app',
                    target="_blank"
                )
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "A multipage app that keeps track of one's investments.",
            size="sm",
            color="dimmed",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

card3 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.im.ge/2024/01/11/3xar3p.your-project-filler.png",
                    alt="dash-app",
                ),
                href="https://charming-data.com/",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("Your Project Title", weight=500, size='xl'),
                html.A(
                    DashIconify(icon="skill-icons:linkedin", width=30),
                    href='https://www.linkedin.com/in/adam-schroeder-17b5a819/',
                    target="_blank"
                )
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Your project description to share with the viewers of your portfolio.",
            size="sm",
            color="dimmed",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

all_cards = [
    dmc.Header(
        height=80,
        children=[dmc.Text("Data Analysis and AI Projects",
                           style={"fontSize": 40})],
    ),
    dmc.SimpleGrid(
        cols=3,
        spacing="lg",
        breakpoints=[
            {"maxWidth": 1240, "cols": 2, "spacing": "md"},
            {"maxWidth": 950, "cols": 1, "spacing": "sm"},
        ],
        children=[
            html.Div(card1),
            html.Div(card2),
            html.Div(card3),
        ],
    )
]

reference_card = html.Div([
    dmc.Card(
        children=[
            dmc.Text("Marge Simpson", weight=500, size='xl'),
            dmc.Text(
                "Pretzel business Owner",
                size="md",
                mb="xs",
            ),
            dmc.Text(
                "when a man's biggest dreams include seconds on dessert, occasional snuggling and sleeping in til noon on weekends, no one man can destroy them.",
                size="sm",
                color="dimmed",
            ),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"width": 350})
    ],
    style={"paddingTop": 40}
)

resume_div = html.Div([
    html.Iframe(src="https://drive.google.com/file/d/15vnaw90FhL21SZypgzzAdY24HxJQMujt/preview",
                width="800", height="480")
    ],
    style={"paddingTop": 40}
)


app = Dash()
server = app.server
app.layout = dmc.MantineProvider(
    theme={"colorScheme": "dark"},
    withGlobalStyles=True,
    children=[
            dmc.Tabs(
        [
            dmc.TabsList(
                [
                    dmc.Tab("Projects", value="projects"),
                    dmc.Tab("Resumé", value="resume"),
                    dmc.Tab("References", value="references"),
                ], style={"paddingRight": 50, "paddingTop": 15}
            ),
            dmc.TabsPanel(children=all_cards, value="projects", pb="xs"),
            dmc.TabsPanel(resume_div, value="resume", pb="xs"),
            dmc.TabsPanel(reference_card, value="references", pb="xs"),
        ],
        value="projects",
        orientation='vertical',
        variant='pills',
    )
])


if __name__=='__main__':
    app.run(debug=False)
