# AccessPaths

Exploring permission chains and least-privilege changes through
graph algorithms and mathematical modelling.

**Status:** Planning — implementation has not started.

## The question

Which permission changes can prevent a compromised account from
reaching a sensitive resource while minimising the cost of those changes?

## An example

Consider a fictional system:

Compromised account → Deployment script → Service account → Sensitive data

An account can modify a deployment script. That script runs under a
service account that can read sensitive data. AccessPaths will model
these relationships and investigate where the chain can be broken.

## Planned first version

- Represent a fictional system as a directed graph.
- Find a path from a compromised account to a sensitive resource.
- Assign a non-negative removal cost to each permission edge.
- Use a minimum-cut algorithm to find the lowest-cost set of edges
  whose removal blocks every path between that account and resource.
- Verify the result with small examples and automated tests.

## Mathematical model

Nodes represent accounts, services, or resources. Directed edges
represent explicitly modelled access or control relationships.

The initial model assumes that relationships can be chained and that
edge-removal costs are additive. These are simplifying assumptions,
not a complete model of real-world permissions.

A minimum-cost cut is optimal for the stated graph and cost model.
It does not automatically guarantee minimal operational disruption.

## Planned evaluation

- Check small graphs against hand-calculated results.
- Verify that the proposed removals block all source-to-target paths.
- Compare results with exhaustive search on tiny graphs.
- Measure how runtime changes as graph size increases.
- Examine whether specified legitimate access paths remain available.

## Scope and limitations

The first version will use synthetic examples. It will not scan systems
or connect to real accounts.

Real systems may include conditional permissions, multiple required
privileges, and dependencies that this initial model cannot express.

## Roadmap

- [ ] Define the first example graph.
- [ ] Implement reachability and path finding.
- [ ] Implement and test minimum-cut analysis.
- [ ] Add reproducible experiments.
- [ ] Add a visual demonstration.
- [ ] Publish findings and limitations.

## License

MIT. See [LICENSE](LICENSE).
