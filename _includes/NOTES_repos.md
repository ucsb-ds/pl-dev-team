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

| Team | Slack | NOTES repo | 
|------|---------|-----|-------|-------|----------|-----------|{% for t in site.teams %}
| {{ t.team }} | [Slack]({{t.slack}}) | [NOTES-{{t.team}}](https://github.com/ucsb-cs156-f24/NOTES-{{t.team}}) |{% endfor %}
