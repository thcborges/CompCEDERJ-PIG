import unittest

from BullsAndCowsGame import BullsAndCowsGame
from Status import Status
from TextUI import TextUI
from WordList import WordList


class BullsAndCowsTest(unittest.TestCase):

    wlist = WordList("palavras.txt")

    def test_Bulls(self):
        game = BullsAndCowsGame(self.wlist, "caixa")
        game.startNewRound()

        condition = game.guess("capaz")
        self.assertEqual(game.getBulls(), "ca***", "bulls 1 => 'ca***'")
        self.assertEqual(game.getCows(), "a", "cows 1 => 'a'")
        self.assertEqual(game.getGeese(), "pz", "geese 1 => 'pz'")
        self.assertEqual(condition, Status.KEEP_TURN, "Status 1 => 'Status.KEEP_TURN")

        condition = game.guess("fosse")
        self.assertEqual(game.getBulls(), "ca***", "bulls 2 => 'ca***'")
        self.assertEqual(game.getCows(), "a", "cows 2 => 'a'")
        self.assertEqual(game.getGeese(), "fose", "geese 2 =. 'fose'")
        self.assertEqual(condition, Status.LOSE_TURN, "Status 2 => Status.LOSE_TURN")

        condition = game.guess("plana")
        self.assertEqual(game.getBulls(), "ca***", "bulls 3 => 'ca***'")
        self.assertEqual(game.getCows(), "a", "cows 3 => 'a'")
        self.assertEqual(game.getGeese(), "", "geese 3 => ''")
        self.assertEqual(condition, Status.INVALID_WORD, "Status 3 => Status.INVALID_WORD")

        condition = game.guess("caixa")
        self.assertEqual(game.getBulls(), "caixa", "bulls 4 => 'caixa'")
        self.assertEqual(game.getCows(), "a", "cows 4 => 'a'")
        self.assertEqual(game.getGeese(), "", "geese 4 => ''")
        self.assertEqual(condition, Status.WIN, "Status 4 => Status.WIN")

    def test_word_list(self):

        self.assertEqual(self.wlist.list4, ['acha', 'acre', 'acto', 'adro', 'afim', 'agem', 'agir', 'agro', 'ajam',
                                            'alfa', 'algo', 'alma', 'alta', 'alto', 'alva', 'alvo', 'além', 'amar',
                                            'amor', 'amém', 'anca', 'anel', 'angu', 'anil', 'anjo', 'ante', 'anti',
                                            'apor', 'apto', 'após', 'aqui', 'arar', 'arco', 'arte', 'asco', 'asno',
                                            'assa', 'asso', 'atar', 'ater', 'ateu', 'ator', 'atém', 'auge', 'aula',
                                            'aura', 'auto', 'aval', 'azar', 'azia', 'azul', 'açaí', 'ação', 'bago',
                                            'baio', 'base', 'bebê', 'beco', 'bela', 'belo', 'bens', 'bobo', 'boia',
                                            'bojo', 'bola', 'bolo', 'boxe', 'breu', 'brio', 'bula', 'buxo', 'cabe',
                                            'cabo', 'cada', 'café', 'cair', 'cais', 'caju', 'cama', 'caos', 'capô',
                                            'caro', 'casa', 'caso', 'caça', 'cear', 'cedo', 'cedê', 'cega', 'cego',
                                            'ceia', 'cela', 'celo', 'cena', 'cepo', 'cera', 'ceta', 'chão', 'cima',
                                            'cimo', 'cite', 'cito', 'coco', 'como', 'cona', 'copa', 'coro', 'cota',
                                            'cova', 'coxa', 'coxo', 'coça', 'crer', 'cruz', 'cujo', 'cume', 'cura',
                                            'dado', 'dano', 'data', 'deus', 'deve', 'dico', 'digo', 'dito', 'doar',
                                            'doce', 'dois', 'dolo', 'domo', 'dona', 'dose', 'dote', 'duro', 'duto',
                                            'edil', 'eita', 'eixo', 'ente', 'ermo', 'erro', 'erva', 'esmo', 'essa',
                                            'esse', 'esta', 'este', 'está', 'evoé', 'face', 'fado', 'fala', 'falo',
                                            'fama', 'fase', 'fato', 'feio', 'fera', 'feto', 'fiar', 'fiel', 'fino',
                                            'fito', 'fixa', 'fixo', 'flor', 'foco', 'foda', 'fofo', 'foge', 'fogo',
                                            'fole', 'fome', 'fora', 'foro', 'frio', 'fuga', 'fulo', 'fumê', 'fuso',
                                            'gado', 'gafe', 'gama', 'gana', 'gare', 'gato', 'gaze', 'gene', 'gole',
                                            'gozo', 'grau', 'grei', 'grão', 'guia', 'gula', 'gume', 'guri', 'haja',
                                            'hall', 'halo', 'hein', 'hera', 'hino', 'hoje', 'hora', 'humo', 'idem',
                                            'idos', 'ilha', 'indo', 'irar', 'irmã', 'irão', 'isso', 'isto', 'item',
                                            'içar', 'jaez', 'jeca', 'jiló', 'jipe', 'joia', 'joio', 'jugo', 'juiz',
                                            'lado', 'lago', 'laia', 'laje', 'lama', 'lato', 'laço', 'leal', 'ledo',
                                            'lema', 'leme', 'leso', 'leva', 'leve', 'leão', 'lida', 'lide', 'liga',
                                            'limo', 'lira', 'liso', 'lixo', 'lodo', 'logo', 'lote', 'luar', 'lume',
                                            'luta', 'luto', 'luxo', 'mago', 'mais', 'mana', 'mané', 'mapa', 'maré',
                                            'maço', 'maçã', 'medo', 'meia', 'meio', 'mera', 'mero', 'mesa', 'meta',
                                            'meça', 'mimo', 'mina', 'mini', 'miss', 'mito', 'moda', 'modo', 'mofo',
                                            'mole', 'mono', 'mora', 'mote', 'moço', 'muar', 'mudo', 'muro', 'nada',
                                            'nata', 'nato', 'nela', 'nenê', 'nexo', 'nojo', 'nome', 'nota', 'novo',
                                            'nulo', 'numa', 'nume', 'obra', 'ocre', 'odor', 'ogra', 'ogro', 'olho',
                                            'olor', 'onda', 'onde', 'opor', 'oral', 'orar', 'orbe', 'orla', 'osso',
                                            'ouro', 'pane', 'papo', 'para', 'país', 'pedi', 'peia', 'pejo', 'pela',
                                            'pele', 'pelo', 'pena', 'pera', 'pesa', 'peso', 'peão', 'peça', 'peço',
                                            'pior', 'pipa', 'pião', 'pneu', 'pode', 'pois', 'poli', 'pomo', 'poro',
                                            'pose', 'povo', 'poxa', 'poça', 'poço', 'proa', 'prol', 'pude', 'puro',
                                            'puta', 'puto', 'pólo', 'qual', 'quem', 'quer', 'quis', 'quão', 'rack',
                                            'raia', 'raio', 'raiz', 'ralé', 'rama', 'ramo', 'raro', 'raso', 'real',
                                            'rede', 'rege', 'reto', 'rico', 'rijo', 'rima', 'riso', 'rito', 'rixa',
                                            'rogo', 'rola', 'rota', 'roto', 'roça', 'rude', 'ruim', 'ruir', 'rumo',
                                            'ruço', 'saga', 'saia', 'sair', 'saiu', 'sapé', 'sebe', 'sebo', 'seca',
                                            'seco', 'seda', 'sede', 'sedo', 'sega', 'seio', 'seja', 'sela', 'selo',
                                            'semi', 'será', 'seta', 'sexo', 'sexy', 'show', 'sido', 'silo', 'sina',
                                            'siso', 'sito', 'soar', 'sobe', 'sofá', 'solo', 'soma', 'sono', 'sopé',
                                            'sova', 'suar', 'sujo', 'suma', 'sumo', 'tabu', 'tais', 'tapa', 'tato',
                                            'taxa', 'teia', 'tema', 'teor', 'tese', 'teso', 'teto', 'teve', 'tido',
                                            'time', 'tino', 'tipo', 'titã', 'todo', 'toga', 'tolo', 'tomo', 'tona',
                                            'topo', 'traz', 'trem', 'trás', 'tudo', 'tufo', 'tupi', 'táxi', 'unir',
                                            'urbe', 'urge', 'usar', 'vaga', 'vago', 'vale', 'valo', 'vara', 'vaso',
                                            'vate', 'veio', 'vela', 'vero', 'veto', 'vida', 'vide', 'virá', 'viva',
                                            'vivo', 'viço', 'viés', 'voar', 'você', 'voga', 'voto', 'vovó', 'vêem',
                                            'xale', 'zelo', 'ágil', 'ágio', 'água', 'área', 'ária', 'éter', 'ócio',
                                            'ódio', 'óleo', 'ópio', 'ônus', 'útil'], "4 letters word list")
        self.assertEqual(self.wlist.list5, ['abrir', 'acaso', 'aceso', 'achar', 'acima', 'adiar', 'advir', 'advém',
                                            'afago', 'afeto', 'afora', 'agudo', 'ainda', 'algoz', 'algum', 'aliás',
                                            'alçar', 'ambas', 'ameno', 'amigo', 'amplo', 'anais', 'anciã', 'anelo',
                                            'anexo', 'antro', 'anuir', 'aonde', 'apego', 'apelo', 'apoio', 'apraz',
                                            'aquém', 'arcar', 'ardil', 'ardor', 'aroma', 'asilo', 'assaz', 'assim',
                                            'astro', 'ativo', 'atroz', 'atrás', 'atuar', 'audaz', 'autor', 'avaro',
                                            'avião', 'banal', 'bando', 'bater', 'beata', 'bicho', 'birra', 'botar',
                                            'boçal', 'brado', 'bravo', 'breve', 'brisa', 'bruma', 'burro', 'cabal',
                                            'cacho', 'caixa', 'calda', 'calma', 'campo', 'canso', 'capaz', 'carro',
                                            'casal', 'casta', 'casto', 'cauda', 'causa', 'caçar', 'ceder', 'censo',
                                            'cerne', 'certa', 'certo', 'cesta', 'cheio', 'chulo', 'ciclo', 'cinto',
                                            'cioso', 'cisma', 'cisão', 'citar', 'ciúme', 'claro', 'clava', 'coeso',
                                            'coisa', 'comer', 'comum', 'corja', 'corpo', 'coser', 'cover', 'covil',
                                            'cozer', 'coçar', 'credo', 'criar', 'crime', 'crise', 'crivo', 'cruel',
                                            'culto', 'cunho', 'cível', 'cópia', 'denso', 'deram', 'desde', 'desse',
                                            'deter', 'detém', 'dever', 'devir', 'digno', 'dizer', 'dogma', 'doido',
                                            'dorso', 'douto', 'doído', 'débil', 'dócil', 'dúbio', 'elite', 'enfim',
                                            'então', 'ereto', 'estar', 'estro', 'estão', 'etnia', 'exame', 'exato',
                                            'exijo', 'expor', 'facto', 'falar', 'falso', 'falta', 'fardo', 'farsa',
                                            'farão', 'fatal', 'fator', 'fauna', 'favor', 'fazer', 'façam', 'feito',
                                            'feixe', 'feliz', 'fenda', 'feudo', 'ficar', 'ficha', 'finda', 'finjo',
                                            'firme', 'fitar', 'fixar', 'flora', 'fluir', 'fluxo', 'folga', 'fonte',
                                            'forem', 'forma', 'forte', 'força', 'fosse', 'fraco', 'fruir', 'fugaz',
                                            'fugir', 'furor', 'fusão', 'fácil', 'fátuo', 'fútil', 'garbo', 'genro',
                                            'gente', 'gerar', 'gerir', 'gesto', 'gleba', 'glosa', 'golpe', 'gozar',
                                            'grato', 'grave', 'graça', 'guisa', 'gênio', 'haste', 'haver', 'havia',
                                            'herói', 'hiato', 'homem', 'honra', 'horda', 'houve', 'hábil', 'ideal',
                                            'ideia', 'igual', 'impor', 'imune', 'inato', 'irmão', 'jazia', 'jeito',
                                            'jovem', 'junto', 'justo', 'juízo', 'labor', 'laico', 'lapso', 'lasso',
                                            'lavra', 'legal', 'leigo', 'leito', 'lesse', 'levar', 'liame', 'lidar',
                                            'ligar', 'limbo', 'lindo', 'logro', 'louco', 'lugar', 'lâmia', 'líder',
                                            'maior', 'malta', 'manso', 'massa', 'matiz', 'mercê', 'mesma', 'mesmo',
                                            'messe', 'mexer', 'moral', 'morar', 'morte', 'motim', 'moção', 'mudar',
                                            'muito', 'mundo', 'mágoa', 'mútua', 'mútuo', 'navio', 'nação', 'negro',
                                            'neném', 'nicho', 'nobre', 'noite', 'noção', 'nível', 'nódoa', 'obter',
                                            'ocaso', 'olhar', 'ontem', 'opaco', 'optar', 'opção', 'ordem', 'orgia',
                                            'outro', 'ouvir', 'oásis', 'paira', 'pajem', 'papel', 'parco', 'pardo',
                                            'parte', 'parvo', 'pasmo', 'passo', 'pauta', 'pecha', 'pedir', 'pegar',
                                            'peixe', 'perda', 'pesar', 'peste', 'plano', 'platô', 'plebe', 'pleno',
                                            'pobre', 'poder', 'pompa', 'ponto', 'porra', 'porém', 'possa', 'posse',
                                            'posso', 'pouco', 'prado', 'praga', 'praia', 'praxe', 'prazo', 'prece',
                                            'presa', 'preso', 'probo', 'prole', 'prosa', 'prova', 'prumo', 'pudor',
                                            'pulha', 'puxar', 'pária', 'pífio', 'quase', 'quite', 'quiçá', 'quota',
                                            'raiva', 'rapaz', 'razão', 'reaça', 'recém', 'reger', 'regra', 'reino',
                                            'reles', 'relva', 'remir', 'reses', 'reter', 'revel', 'rever', 'revés',
                                            'rezar', 'rigor', 'ritmo', 'rival', 'rogar', 'rouca', 'round', 'rubro',
                                            'ruína', 'saber', 'sagaz', 'saiba', 'salvo', 'sanar', 'sarau', 'saruê',
                                            'saída', 'saúde', 'seara', 'segue', 'selar', 'senda', 'sendo', 'senil',
                                            'senso', 'senão', 'seria', 'servo', 'serão', 'sesta', 'setor', 'seção',
                                            'signo', 'sinal', 'sinto', 'sobre', 'soldo', 'solto', 'sonho', 'sonso',
                                            'sulco', 'sumir', 'supor', 'supra', 'sutil', 'sábio', 'série', 'sério',
                                            'súcia', 'tange', 'tanto', 'tecer', 'temer', 'temor', 'tempo', 'tenaz',
                                            'tende', 'tendo', 'tenro', 'tenso', 'termo', 'terno', 'tirar', 'toada',
                                            'tomar', 'torpe', 'torso', 'traga', 'trama', 'traço', 'troça', 'turba',
                                            'turva', 'turvo', 'tédio', 'tênue', 'união', 'usura', 'valha', 'valia',
                                            'valor', 'varão', 'vasto', 'vazio', 'velar', 'velho', 'vemos', 'venal',
                                            'vendo', 'venho', 'verba', 'verso', 'vetor', 'vigor', 'vimos', 'viram',
                                            'viril', 'virão', 'visar', 'visão', 'vital', 'vivaz', 'viver', 'voraz',
                                            'vulgo', 'vulto', 'vácuo', 'vênia', 'vício', 'xeque', 'zelar', 'álibi',
                                            'ápice', 'árduo', 'árido', 'átrio', 'áureo', 'ávido', 'âmago', 'ânimo',
                                            'ânsia', 'ébrio', 'égide', 'épico', 'época', 'ética', 'êxito', 'êxodo',
                                            'ícone', 'ígneo', 'ímpar', 'ímpio', 'índio', 'óbice', 'óbito', 'óbvio',
                                            'órfão', 'ótica', 'ótimo', 'único'], "5 letters word list")


        self.assertEqual(self.wlist.check("algo"), True, "check algo")
        self.assertEqual(self.wlist.check("xyzw"), False, "check xyzw")

        self.assertEqual(self.wlist.check("algoz"), True, "check algoz")
        self.assertEqual(self.wlist.check("qwerty"), False, "check qwerty")

        self.assertEqual(self.wlist.check("chá"), False, "check chá")
        self.assertEqual(self.wlist.check("guloso"), False, "check guloso")

    def text_ui(self):
        ui = TextUI(BullsAndCowsGame(self.wlist, 4))

        self.assertEqual(ui.player, "Jogador 1", "Jogador 1 inicia o jogo")
        ui.change_player()
        self.assertEqual(ui.player, "Jogador 2", "muda para Jogador 2")
        ui.change_player()
        self.assertEqual(ui.player, "Jogador 1", "Retorna para o Jogador 1")

        # Os próximos testes testam o funcionamento de diversos métodos:
        #   - display()
        #   - condition_message()
        #   - spell(word)
        #
        ui.status = Status.START
        self.assertEqual(ui.display(), "||########################||\n"
                                       "||    BULLS AND COWS      ||\n"
                                       "||         GAME           ||\n"
                                       "||########################||\n"
                                       "\n"
                                       "  - Bulls:  * * * *\n"
                                       "  - Cows:\n"
                                       "  - Gansos:\n"
                                       "  - Chutes:\n"
                                       "\n"
                                       "Novo jogo\n"
                                       "\n"
                                       "Jogador 1\n", "tela do jogo com mensagem de novo jogo")

        ui.status = Status.INVALID_WORD
        self.assertEqual(ui.display(), "||########################||\n"
                                       "||    BULLS AND COWS      ||\n"
                                       "||         GAME           ||\n"
                                       "||########################||\n"
                                       "\n"
                                       "  - Bulls:  * * * *\n"
                                       "  - Cows:\n"
                                       "  - Gansos:\n"
                                       "  - Chutes:\n"
                                       "\n"
                                       "Essa palavra não existe em nosso dicionário.\n"
                                       "\n"
                                       "  - PRÓXIMO JOGADOR\n"
                                       "\n"
                                       "Jogador 1\n", "tela do jogo com mensagem de palavra inválida")

        ui.status = Status.LOSE_TURN
        self.assertEqual(ui.display(), "||########################||\n"
                                       "||    BULLS AND COWS      ||\n"
                                       "||         GAME           ||\n"
                                       "||########################||\n"
                                       "\n"
                                       "  - Bulls:  * * * *\n"
                                       "  - Cows:\n"
                                       "  - Gansos:\n"
                                       "  - Chutes:\n"
                                       "\n"
                                       "Nenhum touro no chute.\n"
                                       "\n"
                                       "  - PRÓXIMO JOGADOR\n"
                                       "\n"
                                       "Jogador 1\n", "tela do jogo com mensagem de perda de turno")

        ui.status = Status.KEEP_TURN
        self.assertEqual(ui.display(), "||########################||\n"
                                       "||    BULLS AND COWS      ||\n"
                                       "||         GAME           ||\n"
                                       "||########################||\n"
                                       "\n"
                                       "  - Bulls:  * * * *\n"
                                       "  - Cows:\n"
                                       "  - Gansos:\n"
                                       "  - Chutes:\n"
                                       "\n"
                                       "Muito bem!\n"
                                       "\n"
                                       " Continue jogando"
                                       "\n"
                                       "Jogador 1\n", "tela do jogo com mensagem de manter o turno")


        ui.status = Status.WIN
        self.assertEqual(ui.display(), "||########################||\n"
                                       "||    BULLS AND COWS      ||\n"
                                       "||         GAME           ||\n"
                                       "||########################||\n"
                                       "\n"
                                       "  - Bulls:  * * * *\n"
                                       "  - Cows:\n"
                                       "  - Gansos:\n"
                                       "  - Chutes:\n"
                                       "\n"
                                       "PARABÉNS!!!\n"
                                       "Jogador 1\n"
                                       "VENCEU O JOGO!\n"
                                       "\n"
                                       "Jogador 1\n", "tela do jogo com mensagem de vitória do Jogador 1")

        # A função check_size() e os método playAgain() e runUI()
        # eu não sei testar. Nem sei se é possível.
        # Porém fiz os testes do jogo manualmente também
        # e tudo funionou conforme esperado.



if __name__ == '__main__':
    unittest.main()
