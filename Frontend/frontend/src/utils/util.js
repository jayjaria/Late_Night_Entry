const store = window.localStorage;
export function saveToStore(key, value) {
  store.setItem(key, value);
}

export function getFromStore(key) {
  return store.getItem(key);
}

export function removeFromStore(key) {
  store.removeItem(key);
}

export function clearStorage() {
  store.clear();
}
