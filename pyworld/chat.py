import jieba
import re

class ChatBot:
    def __init__(self, language='zh', model_path=None):
        self.language = language
        self.model_path = model_path
        self.jieba = jieba
        self.conversation_history = []
        self.initialize()
    
    def initialize(self):
        if self.language == 'zh':
            jieba.initialize()
        self.responses = {
            '你好': '你好！很高兴认识你。',
            '谢谢': '不客气！',
            '再见': '再见！',
            '帮助': '我可以帮你进行对话交互。',
        }
    
    def tokenize(self, text):
        if self.language == 'zh':
            return list(self.jieba.cut(text))
        else:
            return text.split()
    
    def talk(self, message):
        if not isinstance(message, str):
            return "Error: Input must be a string"
        
        message = message.strip()
        self.conversation_history.append(('user', message))
        
        response = self._generate_response(message)
        self.conversation_history.append(('bot', response))
        return response
    
    def _generate_response(self, message):
        for key, value in self.responses.items():
            if key in message:
                return value
        return "I understand you said: " + message + ". Please continue."
    
    def get_history(self):
        return self.conversation_history
    
    def clear_history(self):
        self.conversation_history = []
    
    def add_response(self, trigger, response):
        self.responses[trigger] = response