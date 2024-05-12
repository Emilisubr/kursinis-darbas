Coursework Report: Tic Tac Toe Game
1. Introduction
a. What is your application?
Kodas parašytas python kalba, kuris leidžia žaisti žaidima Tic Tac Toe. Žaidimas vyksta kol kažkuris žaidėjas laimi, arba yra lygiosios.

b. How to run the program?
Reikia turėti python savo kompiuteryje ir kodą galima paleisti per programas palaikančias python.

c. How to use the program?
Yra nurodymai kaip žmogus turi elgtis, jo ėjimo metu.

2. Body/Analysis
a. Explain how the program covers functional requirements
The program implements the following functional requirements:

Encapsulation:„HumanPlayer“, „ComputerPlayer“ ir „TicTacToe“ klasės apima duomenis (atributus) ir elgseną (metodai).
Tokie atributai kaip vardas, simbolis, lenta ir current_player yra įtraukiami į atitinkamas klases.
Tokie metodai kaip make_move, print_board, check_winner, check_tie ir switch_players apima elgseną, susietą su objektais.
Abstraction: Player klasė apibrėžia abstraktų metodą make_move, kuris suteikia bendrą sąsają visiems žaidėjams.
Inheritance:HumanPlayer ir ComputerPlayer paveldi iš Player klasės, paveldi jos atributus ir abstraktų metodą.
Polymorphism: demonstruojamas naudojant make_move metodą. HumanPlayer ir ComputerPlayer laikosi to pačio metodo aprašo, kaip apibrėžta Player klasėje.

Design patterns:
Factory Method Pattern:PlayerFactory apibrėžia create_player metodą, leidžiantį poklasiams kurti skirtingų Player tipų (HumanPlayer ir ComputerPlayer) egzempliorius, neatskleidžiant kūrimo logikos klientui.
Strategy Pattern: Žaidėjų klasė apibrėžia make_move metodą kaip abstraktų metodą, kuris yra strategijos sąsaja.
„HumanPlayer“ ir „ComputerPlayer“ pateikia konkrečius make_move metodo įgyvendinimus, atspindinčius skirtingas strategijas, kaip atlikti žaidimus „Tic Tac Toe“.

3. Results 
Žaidimą Tic Tac Toe sukūriau sėkmingai, tačiau nevisai taip kaip norėjau. Žaidimas veikia iki kol yra laimėtojas arba yra lygiosios. Sunkiausia buvo padaryti testus, ir buvo daug neaiškiu vietų kursinio darbo metu. Neaišku buvo kaip įkelti i github visą darbą, bei neaišku kaip reikia ta darbą pushinti ir kaip elgtis su githubu.

