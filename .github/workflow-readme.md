## What this workflow does
This workflow will create a new draft release automatically for you, given a couple of inputs for the tag and optionally
the title. It will then automatically attach the files from the repository needed for the user to patch the game and
generate the AP world to the release draft created. This is important for a few reasons:
- We don't want to have drift between what is uploaded to the release and what is actual code in the repository.
- Creates one source of truth for the release assets, which are only files within the repository itself.
- Standardizes release structure, to ensure minimal confusion to the consumer when attempting to download a release.

## How to use this workflow:

1. Navigate to the Actions tab of the repository.
2. On the left, you will see a sidebar labeled "Actions" at the top. You'll want to click on the workflow on the left 
   called "Release Drafter", which will list out the result of the executions of the action.
3. You should see a banner that says "This workflow has a workflow_dispatch event trigger", and on the right of that 
   banner you should see a dropdown context menu labeled "Run workflow"
   - You'll want to use workflow from main, usually, but you could pick any branch
4. You should see an input window with two string inputs:
   - `release_tag`: Required, should ideally be [SemVer](https://semver.org/) like `v.0.1.2` but you can make it 
     anything within the constraints of GitHub tag naming in actuality.
   - `release_title`: Optional, defaults to release_tag, but if you want to modify it, you can.
5. Once you've given input, click Run workflow. You should now see the workflow execution running. If it fails, you can 
   check the execution for logs on a reason why. Else if it succeeds, your draft has been created.
6. Navigate to the releases page of the GitHub. You should see the created draft at the top. This draft is not public.
   Click on the pencil icon on the top right of the draft to edit it. Verify that the tag/title are correct, that all
   the files are attached, and feel free to add details on change notes as you like. 
7. Once finished, you can create the release, and you're done!

If you've made a mistake to the tag or anything on generation, you can just delete the release, or you can edit the
draft that was created to be corrected.

The only error that should happen is if you specify a tag that already exists- there will be a conflict, and the
release draft should not be created in that case.

## Security Concerns?
Anyone who has `write` access to the repository may run this workflow. This is a GitHub standard, I believe. 
If you wish to lock-down the action to only yourself, you can modify it as such:

```
jobs:
  create_release_draft:
    if: github.actor == 'owner_username' # add this line
    runs-on: ubuntu-latest
```

Replacing `owner_username` with your own. But at that point, someone with `write` access could just write to the file
and remove that line. If you'd *really* want to lock it down, you'd also have to ensure that your main branch is
protected from any pushes to require a PR with approval, and then also modify the if statement to this:

```
if: github.ref == 'refs/heads/main' && github.actor == 'owner_username'
```

Up to you if you feel this is necessary.