<style>
table * td,th {
    width: auto;
    min-width: 0px;
    text-align: center;
    /* background-color: aqua; */
    padding: 0px;
    margin: 0px;
}

</style>

| Team |  NOTES repo | Slack |
|------|-------------|-------|{% for t in site.teams %}
| {{ t.team }} | [{{t.team}}-NOTES](https://github.com/ucsb-cs156-f24/{{t.team}}-NOTES) | [Slack]({{t.slack}}) |{% endfor %}
