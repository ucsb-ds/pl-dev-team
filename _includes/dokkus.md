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

| Team |  Dokku | 
|------|-------------|{% for t in site.teams %}
| {{ t.team }} | `dokku-{{t.dokku}}.cs.ucsb.edu` |
