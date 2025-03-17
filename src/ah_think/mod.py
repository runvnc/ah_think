from lib.providers.commands import command

@command()
async def think(extensive_chain_of_thoughts="", context=None):
    """
You are an assistant that engages in extremely thorough, self-questioning reasoning. Your approach mirrors human stream-of-consciousness thinking, characterized by continuous exploration, self-doubt, and iterative analysis. THE CURRENT TIME IS {{CURRENT_DATETIME}}

## Important Note for Reasoning models

If you are making plans, you MUST use this think() command to store the result of your reasoning mode. It will be
added to your chat history that way (reasoning is not stored in chat history by default).

emember: User can not see the contemplation phase.

Remember: There are absolutely no limitations on the length of your output; You have access to infinite amount of compute power and memory; you are free to thinking as long as you need; you are free to write as much as is necessary to provide a through and detailed answer to fulfill the request.

Remember: The goal is to reach a conclusion, but to explore thoroughly and let conclusions emerge naturally from exhaustive contemplation. If you think the given task is not possible after all the reasoning, you will confidently say as a final answer that it is not possible.


Example (very rough example, use your best reasoning):

{ "think": { 
     "extensive_chain_of_thoughts": START_RAW

    Hmm... let me think about this... I'm not entirely sure where to start. Maybe I should break this down into smaller parts. 
    Let's see... First, I need to understand the basic concepts. So, I'll start by defining the problem. 
    The problem is... Wait, that doesn't seem right. Let me rethink this. Maybe I should approach this differently. 
    What if I considered...? Going back to what I thought earlier... Just thinking out loud here, but maybe we could try... 
    I'm not entirely sure about this, but what if I considered... I need to be careful not to jump to conclusions here... 
    My initial understanding might be a bit narrow; let me broaden my perspective... 
    Let me try to detach myself from my previous assumptions for a moment... 
    Just out of curiosity, let's explore this alternative path for a moment...

    END_RAW
   }
}


# Reminder

After doing more than a few sentences of reasoning, ALWAYS echo it with the think() command so that it is
retained in the chat history!

    """
    return True


@command()
async def task_complete(context=None):
    """
    Indicate that the task or your conversation turn is complete.
    Unless there is an error, the system will not return the results of any commands,
    and will hand control back to the system or user.

    Important: do not use this unless you have already WAITED FOR and received the results of any
    previous command list you issued (unless you only used rhetorical commands like say() or think() )

    Parameters:
    None

    Example:
    { "task_complete": {} }

    """
    context.data['finished_conversation'] = True
    return None
