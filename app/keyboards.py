from mybot import router
from rocketgram import MessageType, ReplyKeyboard, ReplyKeyboardRemove
from rocketgram import context, commonfilters, ChatType, SendMessage


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.command('/keyboard')
async def keyboard_command():
    """Shows how to create reply keyboard"""

    kb = ReplyKeyboard()
    kb.text("๐ Super").row()
    kb.text("๐ Great").row()
    kb.text("๐คจ Not bad").row()
    kb.text("๐ All bad").row()
    kb.text("/cancel")

    await SendMessage(context.user.id, '๐น How are you feeling?', reply_markup=kb.render()).send()


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.command('/keyboard_location')
async def keyboard_location_command():
    """Shows how to create location button"""

    kb = ReplyKeyboard()
    kb.location("๐บ Send location").row()
    kb.text("/cancel")

    await SendMessage(context.user.id, '๐น Send me your location.', reply_markup=kb.render()).send()


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.message_type(MessageType.location)
async def got_location():
    """Reaction on location"""

    await SendMessage(context.user.id,
                      '๐น Now i known where are you. ๐',
                      reply_markup=ReplyKeyboardRemove(),
                      reply_to_message_id=context.message.message_id).send()


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.command('/keyboard_contact')
async def keyboard_contact_command():
    """Shows how to create contact button"""

    kb = ReplyKeyboard()
    kb.contact("โ๏ธ Send contact").row()
    kb.text("/cancel")

    await SendMessage(context.user.id, '๐น Send me your contact.', reply_markup=kb.render()).send()


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.message_type(MessageType.contact)
async def got_contact():
    """Reaction on contact"""

    await SendMessage(context.user.id,
                      '๐น Now i known your phone. ๐',
                      reply_markup=ReplyKeyboardRemove(),
                      reply_to_message_id=context.message.message_id).send()


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.command('/cancel')
def cancel_command():
    """Removes current reply keyboard"""

    SendMessage(context.user.id, "๐น What's next?", reply_markup=ReplyKeyboardRemove()).webhook()
