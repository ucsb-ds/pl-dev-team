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
| {{ t.team }} | [NOTES-{{t.team}}](https://github.com/ucsb-cs156-s25/NOTES-{{t.team}}) | [Slack]({{t.slack}}) |{% endfor %}
