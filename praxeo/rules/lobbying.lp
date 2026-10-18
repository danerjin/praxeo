% RS-7's Unless clause (catalog 1.0, 1.1; CR-4 1.0, 1.1). Where the policy field the measure settles (rent regulation, farm
% support) was contested before it and would stay contested without it, lobbying on that question happens in both worlds:
% each class's lobbying on it is signed against that contest, and the sign is ambiguous without a premise. Lobbying over
% provisions that exist only under the measure stays an increase (CR-4 1.1), so the contested question is a separate item,
% `policy_field`, beside the ordinary row (WE-067 C-26 and C-27; WE-065 C-15 and C-36). No total is formed over the two.
% Input facts: field_contested(C), set from Component.field_contested; the premise contested_otherwise(C) says the
% question would have stayed contested on the counterfactual path.
% Each lobbying conclusion of the other rule files is listed with its component.

lobby_concl(lobbying(C), C)           :- lobbying(C).
lobby_concl(lobbying_protected(C), C) :- lobbying_protected(C).
lobby_concl(tx_lobbies_sellers(C), C) :- tx_lobbies_sellers(C).
lobby_concl(tx_lobbies_users(C), C)   :- tx_lobbies_users(C).
lobby_concl(sb_lobbies(C), C)         :- sb_lobbies(C).
lobby_concl(en_lobby(C), C)           :- en_lobby(C).

contested_lobby(X) :- lobby_concl(X, C), field_contested(C), holds(contested_otherwise(C)), not exception(rs_7, C).
fired(rs_7, contested_lobby(X), X)                     :- contested_lobby(X).
fired(rs_7, contested_lobby(X), contested_otherwise(C)) :- contested_lobby(X), lobby_concl(X, C).
effect(contested_lobby(X), A, "lobbying_effort", ambiguous, H, V, T) :- contested_lobby(X), effect(X, A, "lobbying_effort", increase, H, V, T).
item(contested_lobby(X), "policy_field") :- contested_lobby(X).

#show holds/1.
#show fired/3.
#show effect/7.
#show group_effect/7.
#show window/2.
#show item/2.
