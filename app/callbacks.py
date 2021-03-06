from mybot import router
from rocketgram import InlineKeyboard
from rocketgram import SendMessage, AnswerCallbackQuery, DeleteMessage
from rocketgram import commonfilters, ChatType, context


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.command('/simple_inline_keyboard')
async def simple_inline_keyboard():
    """Shows how to create inline keyboard."""

    kb = InlineKeyboard()
    kb.callback("๐ Super", 'simple 1').row()
    kb.callback("๐ Great", 'simple 2').row()
    kb.callback("๐คจ Not bad", 'simple 3').row()
    kb.callback("๐ All bad", 'simple 4').row()
    kb.callback("โ Close", 'simple close')

    await SendMessage(context.user.id, '๐น How are you filling?', reply_markup=kb.render()).send()


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.callback('simple')
async def reaction_on_simple_keyboard():
    """Reaction on simple keyboard."""

    variant = context.callback.data.split()[1]

    if variant == 'close':
        await AnswerCallbackQuery(context.callback.id).send()
        await DeleteMessage(context.chat.id, context.message.message_id).send()
        return

    answers = {
        '1': '๐น Super, Ok!',
        '2': '๐น Great, Ok!',
        '3': '๐น Ok!',
        '4': '๐น Sad!',
    }

    msg = answers[variant]

    await AnswerCallbackQuery(context.callback.id, msg, show_alert=True).send()


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.command('/arranged_inline_keyboard')
async def arranged_simple_inline_keyboard():
    """Shows how to arrange inline keyboard."""

    kb = InlineKeyboard()

    for i in range(30):
        kb.callback("%s" % i, 'arranged %s' % i)

    kb.callback("โ Close", 'arranged close')

    kb.arrange_simple(5)

    await SendMessage(context.user.id, '๐น Select number.', reply_markup=kb.render()).send()


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.callback('arranged')
async def reaction_on_simple_keyboard():
    """Reaction on arranged simple keyboard"""

    variant = context.callback.data.split()[1]

    if variant == 'close':
        await AnswerCallbackQuery(context.callback.id).send()
        await DeleteMessage(context.chat.id, context.message.message_id).send()
        return

    msg = '๐น Selected: %s' % variant

    await AnswerCallbackQuery(context.callback.id, msg).send()


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.command('/arranged_scheme_inline_keyboard')
async def arranged_simple_inline_keyboard():
    """Shows how to arrange inline keyboard by scheme."""

    kb = InlineKeyboard()

    kb.callback("โช Prev", 'scheme prev')
    kb.callback("โ Do!", 'scheme do')
    kb.callback("Next โฉ", 'scheme next')

    for i in range(60):
        kb.callback("%s" % i, 'scheme %s' % i)

    kb.callback("โ Close", 'scheme close')

    kb.arrange_scheme(3, 6, 1)

    await SendMessage(context.user.id, '๐น Select number.', reply_markup=kb.render()).send()


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.callback('scheme')
async def reaction_on_simple_keyboard():
    """Reaction on arranged simple keyboard."""

    variant = context.callback.data.split()[1]

    if variant == 'close':
        await AnswerCallbackQuery(context.callback.id).send()
        await DeleteMessage(context.chat.id,
                            context.message.message_id).send()
        return

    if variant == 'do':
        await AnswerCallbackQuery(context.callback.id, '๐น Doing something', show_alert=True).send()
        return

    if variant == 'prev':
        await AnswerCallbackQuery(context.callback.id, '๐น Showing previous page', show_alert=True).send()
        return

    if variant == 'next':
        await AnswerCallbackQuery(context.callback.id, '๐น Showing next page', show_alert=True).send()
        return

    msg = '๐น Selected: %s' % variant

    await AnswerCallbackQuery(context.callback.id, msg).send()
