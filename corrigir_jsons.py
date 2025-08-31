import os
import json
import re

# --- A Nova e Robusta Função de Extração ---
def extract_json_from_response(text):
    """
    Extrai de forma robusta um bloco de código JSON da resposta de um LLM,
    mesmo que esteja mal formatado com markdown ou tenha texto extra.
    """
    # 1. Tenta encontrar o bloco JSON usando uma expressão regular flexível
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        json_str = match.group(0)
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            pass # Se a regex falhar, o erro será tratado abaixo

    # 2. Se a regex falhar, tenta carregar o texto inteiro (plano B)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None # Retorna None se nada funcionar
    except Exception:
        return None

# --- Lógica Principal do Script de Correção ---

if __name__ == "__main__":
    outputs_dir = 'outputs'
    total_files_checked = 0
    total_files_fixed = 0
    failed_files = []

    print("--- Iniciando o script de correção de JSONs ---")

    # `os.walk` percorre todas as pastas e subpastas
    for root, dirs, files in os.walk(outputs_dir):
        for filename in files:
            if filename.endswith('.json'):
                total_files_checked += 1
                file_path = os.path.join(root, filename)

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    # Verifica se o arquivo tem a nossa marca de erro
                    if isinstance(data, dict) and data.get("error") == "Invalid JSON response":
                        print(f"Encontrado arquivo com erro: {file_path}")
                        raw_response = data.get("raw_response", "")

                        if raw_response:
                            # Tenta corrigir usando a nova função
                            corrected_json = extract_json_from_response(raw_response)

                            if corrected_json:
                                # Se a correção funcionou, sobrescreve o arquivo
                                with open(file_path, 'w', encoding='utf-8') as f:
                                    json.dump(corrected_json, f, ensure_ascii=False, indent=2)
                                print(f"  -> SUCESSO: Arquivo corrigido e salvo!")
                                total_files_fixed += 1
                            else:
                                # Se a nova função também falhou
                                print(f"  -> FALHA: Não foi possível extrair um JSON válido da resposta bruta.")
                                failed_files.append(file_path)
                        else:
                            print(f"  -> FALHA: Arquivo de erro não continha 'raw_response'.")
                            failed_files.append(file_path)

                except Exception as e:
                    print(f"Erro ao processar o arquivo {file_path}: {e}")
                    failed_files.append(file_path)

    print("\n--- Script de correção concluído! ---")
    print(f"Total de arquivos .json verificados: {total_files_checked}")
    print(f"Total de arquivos corrigidos: {total_files_fixed}")

    if failed_files:
        print("\nOs seguintes arquivos não puderam ser corrigidos e podem precisar de análise manual:")
        for path in failed_files:
            print(f"- {path}")