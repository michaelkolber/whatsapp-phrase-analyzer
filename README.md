# WhatsApp Phrase Analyzer
A simple tool for analyzing phrase usage between participants in a **private** WhatsApp chat. This currently only works for two-person chats.

## Known Issues
- Embedded uses of the phrase do not register. For example, when searching for `dog`, the first `dog` in `dogdog` and the only `dog` in `doggone` will not register (although `dog!`, `bigdog`, and `dog?`, etc. will register). For `dogdog`, it may be desirable to count it. For `doggone`, it is not (since we're looking for a phrase, not a specific collection of letters). Since the latter example seems to be more common, I have decided not to count any embedded words overall. If you know of a better solution, please let me know!
- This only works for two-person chats. It was a quick project but should be fairly trivial to expand to any number of users.
