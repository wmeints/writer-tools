// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from "vscode";
import { ApiClient } from "./api-client";

export function getCurrentDocumentContent(editor: vscode.TextEditor) {
  const document = editor.document;
  const content = document.getText();

  return content;
}

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
  let generateConclusionCmd = vscode.commands.registerCommand(
    "writer-tools.generateConclusion",
    () => {
      const config = vscode.workspace.getConfiguration("writer-tools");

      const apiClient = new ApiClient(
        config.get("endpoint") || "http://localhost:5000",
        config.get("apiKey") || ""
      );

      const editor = vscode.window.activeTextEditor;

      if (!editor) {
        return;
      }

      const content = getCurrentDocumentContent(editor);

      apiClient
        .generateConclusion(content || "")
        .then((conclusion) => {
          editor.edit((editBuilder) => {
            editBuilder.insert(editor.selection.end, conclusion);
          });
        })
        .catch((error) => {
          vscode.window.showErrorMessage(error.message);
        });
    }
  );

  let generateIntroductionCmd = vscode.commands.registerCommand(
    "writer-tools.generateIntroduction",
    () => {
      const config = vscode.workspace.getConfiguration("writer-tools");

      const apiClient = new ApiClient(
        config.get("endpoint") || "http://localhost:5000",
        config.get("apiKey") || ""
      );

      const editor = vscode.window.activeTextEditor;

      if (!editor) {
        return;
      }

      const content = getCurrentDocumentContent(editor);

      apiClient
        .generateIntroduction(content || "")
        .then((introduction) => {
          console.log(introduction);

          editor.edit((editBuilder) => {
            editBuilder.insert(editor.selection.end, introduction);
          });
        })
        .catch((error) => {
          vscode.window.showErrorMessage(error.message);
        });
    }
  );

  context.subscriptions.push(generateConclusionCmd);
  context.subscriptions.push(generateIntroductionCmd);
}

// This method is called when your extension is deactivated
export function deactivate() {}
