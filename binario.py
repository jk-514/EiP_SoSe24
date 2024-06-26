b1 = [[0, 0, 0, 2, 0, 0],
      [1, 0, 1, 0, 0, 0],
      [0, 2, 0, 2, 0, 2],
      [0, 0, 0, 0, 0, 0],
      [1, 0, 0, 2, 0, 0],
      [0, 0, 1, 0, 0, 0]]

b2 = [[0, 1, 2, 0, 0, 2, 1, 1, 0, 1],
      [0, 2, 1, 2, 0, 0, 1, 0, 1, 1],
      [1, 2, 0, 0, 0, 0, 2, 1, 0, 2],
      [0, 1, 2, 0, 0, 1, 0, 0, 2, 0],
      [2, 0, 0, 0, 2, 0, 1, 2, 1, 0],
      [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
      [0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 0, 2, 1],
      [1, 0, 2, 1, 0, 2, 2, 0, 2, 0]]

b3 = [[2, 1, 0, 0, 1, 0, 1, 1, 0, 1],
      [2, 0, 1, 2, 0, 0, 1, 0, 0, 0],
      [0, 2, 0, 0, 2, 0, 0, 0, 0, 2],
      [2, 0, 1, 0, 0, 0, 0, 0, 2, 0],
      [0, 0, 2, 0, 2, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 2, 0, 0, 0, 1, 2],
      [0, 0, 2, 0, 2, 0, 0, 0, 0, 0],
      [0, 2, 0, 0, 0, 0, 2, 0, 1, 0],
      [1, 1, 0, 1, 0, 2, 0, 0, 0, 2]]

"""
def vervollständige(Konfiguration K):
    if vollständig(K) then
        return True
    end

    for each Erweiterungsmöglichkeit E do
        erweitere (K, E)
        if zulässig(K) then
            if vervollständige(K) then
                return True
            end
        end
        mache rückgängig(K, E)
    end
    return False

"""

