Practice writing effective postmortems
======================================

Although everyone strives to ensure there are never any problems, incidents inevitably arise—no matter how fail-safe we feel our code or systems are. Third-party service providers may go down, an update may not perform as expected, or a server may experience a hacking attack. Triaging to resolve the situation is of course important, but it’s also important to document exactly what happened. By doing so, we can prepare if something similar happens in the future. We can also ensure that information shared with management, users, or other affected parties is consistent and clear.

The basics
----------

Postmortems are documents that describe what happened, who and what was affected, how it was resolved, and what the takeaways are. The purpose is to highlight what worked well, as well as learn from what didn’t.

The main sections of the document should follow a pattern similar to the following:

1. What happened and when

2. Who was affected

3. What the root cause was

4. How the issue was resolved and when

5. Why it happened, including improvement plans or other remediation actions

Postmortems can occur for incidents both small and large. Here’s a good [example of a postmortem report](https://status.cloud.google.com/incident/compute/17007#5659118702428160) from a Google incident.

Try creating one for something that happened to you recently!

Tips
----

Different companies and departments handle postmortem documentation differently: You might have a form or template that you update through the incident, a designated project manager or documentarian to track updates, or a formal root-cause analysis (RCA) or postmortem meeting. Whatever system you use, you want to ensure the documentation is useful for the intended audience. In many cases, the audience is the general public or executives, so remember to keep the technical language and acronyms to a minimum.

Writing documentation can be something not everyone enjoys, but it doesn’t have to be complicated. Keep the language simple and concise: Use short sentences and basic language. Focus only on the important information you need to capture: the who, what, how, when, and why.

Remember to stick to the facts. List everything that is necessary to understand the overall picture, but avoid conjecture, blame, or glossing over necessary details. Be honest and accurate about what happened.

The documentation doesn’t need to be deeply detailed or a minute-by-minute recount—just as long as it captures the important information.

You can find some other helpful tips in [this article](https://postmortems.pagerduty.com/how_to_write/effective_postmortems).
