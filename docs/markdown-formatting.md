---
tags:
    - 'general'
---


# Markdown formatting

## Highlight specific lines of code

``` py hl_lines="2 3"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```

## Annotate your code blocks

``` yaml
theme:
  features:
    - content.code.annotate #! (1)
```

1. I'm a code annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be written in Markdown.

## Content tabs

=== "Tab 1"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

=== "Tab 2"

    Phasellus posuere in sem ut cursus

## Tasklist

- [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
- [ ] Vestibulum convallis sit amet nisi a tincidunt
    * [x] In hac habitasse platea dictumst
    * [x] In scelerisque nibh non dolor mollis congue sed et metus
    * [ ] Praesent sed risus massa
- [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque

## Buttons

[:material-laptop: Development](dev/index.md){ .md-button .md-button--primary }

[:material-palette: Design](design/index.md){ .md-button .md-button--primary }

[:material-magnify: Research](research/index.md){ .md-button .md-button--primary }

[:material-chart-bar: Data Science](data/index.md){ .md-button .md-button--primary }

[:material-notebook-multiple: Content Writing](content/index.md){ .md-button .md-button--primary }

[:material-chart-timeline: Product & Project Management](product/index.md){ .md-button .md-button--primary }

## Mermaid

### Using flowcharts

[Flowcharts] are diagrams that represent workflows or processes. The steps
are rendered as nodes of various kinds and are connected by edges, describing
the necessary order of steps:

```` markdown title="Flow chart"
``` mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```
````

<div class="result" markdown>

``` mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```

</div>

  [Flowcharts]: https://mermaid-js.github.io/mermaid/#/flowchart

### Using sequence diagrams

[Sequence diagrams] describe a specific scenario as sequential interactions
between multiple objects or actors, including the messages that are exchanged
between those actors:

```` markdown title="Sequence diagram"
``` mermaid
sequenceDiagram
  autonumber
  Alice->>John: Hello John, how are you?
  loop Healthcheck
      John->>John: Fight against hypochondria
  end
  Note right of John: Rational thoughts!
  John-->>Alice: Great!
  John->>Bob: How about you?
  Bob-->>John: Jolly good!
```
````

<div class="result" markdown>

``` mermaid
sequenceDiagram
  autonumber
  Alice->>John: Hello John, how are you?
  loop Healthcheck
      John->>John: Fight against hypochondria
  end
  Note right of John: Rational thoughts!
  John-->>Alice: Great!
  John->>Bob: How about you?
  Bob-->>John: Jolly good!
```

</div>

  [Sequence diagrams]: https://mermaid-js.github.io/mermaid/#/sequenceDiagram

### Using state diagrams

[State diagrams] are a great tool to describe the behavior of a system,
decomposing it into a finite number of states, and transitions between those
states:

```` markdown title="State diagram"
``` mermaid
stateDiagram-v2
  state fork_state <<fork>>
    [*] --> fork_state
    fork_state --> State2
    fork_state --> State3

    state join_state <<join>>
    State2 --> join_state
    State3 --> join_state
    join_state --> State4
    State4 --> [*]
```
````

<div class="result" markdown>

``` mermaid
stateDiagram-v2
  state fork_state <<fork>>
    [*] --> fork_state
    fork_state --> State2
    fork_state --> State3

    state join_state <<join>>
    State2 --> join_state
    State3 --> join_state
    join_state --> State4
    State4 --> [*]
```

</div>

  [State diagrams]: https://mermaid-js.github.io/mermaid/#/stateDiagram

### Setting direction of State Diagrams

```` markdown

``` mermaid
stateDiagram
    direction LR
    [*] --> A
    A --> B
    B --> C
    state B {
      direction LR
      a --> b
    }
    B --> D
```
````

<div class="result" markdown>

``` mermaid
stateDiagram
    direction LR
    [*] --> A
    A --> B
    B --> C
    state B {
      direction LR
      a --> b
    }
    B --> D
```

</div>

### Comments

Use html comment syntax in your markdown pages:

```html

<!-- This is a comment to be replaced later -->

```

### Tip: Update Markdownlint settings in VSCode

1. Open your VSCode settings by clicking on the gear icon in the lower left corner and selecting "Settings" or by pressing Ctrl + , (Cmd + , on macOS).
2. In the search bar, type "markdownlint" to filter the settings related to markdownlint.
3. Click on "Edit in settings json" under the "Markdownlint: Config" option. This will open your settings. Json file.
4. In the settings. son file, add or update the "markdownlint config" property to include the desired configuration for the MD004 and MD007 rule.

``` json

  "markdownlint.config": {
    "MD004": false, 
    "MD007": false 
  }

```

This configuration will allow you to use mixed styles for unordered lists. Save the settings.json file, and VSCode should now recognize your markdown unordered list formatting as valid and not autocorrect it when you save.
