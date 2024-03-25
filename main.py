from prezentare.consola import UI
from domain.blackjack import Blackjack
from domain.jucator import Jucator
from business.serviceblackjack import ServiceBlackjack
from business.carti import StrCarti
from infrastructura.repo_jucator import RepoJucator
from infrastructura.repo_dealer import RepoDealer


if __name__ == '__main__':
    repo_dealer = RepoDealer()
    repo_jucator = RepoJucator()

    serviceblackjack = ServiceBlackjack(repo_dealer,repo_jucator)

    consola = UI(serviceblackjack)

    consola.start_joc()