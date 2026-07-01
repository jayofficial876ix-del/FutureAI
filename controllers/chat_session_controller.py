class ChatSessionController:

    def send(self, message_box):
        """Send a message and start the conversation flow."""
        conversation = self._build_conversation()
        self._handle_attachment()
        self._stream_response()
        self._save_response()
        return conversation

    def _build_conversation(self):
        """Build the conversation payload from the message box."""
        raise NotImplementedError("_build_conversation must be implemented")

    def _handle_attachment(self):
        """Handle attachments included in the message."""
        raise NotImplementedError("_handle_attachment must be implemented")

    def _stream_response(self):
        """Stream the response back to the user."""
        raise NotImplementedError("_stream_response must be implemented")

    def _save_response(self):
        """Save the response to persistent storage."""
        raise NotImplementedError("_save_response must be implemented")
