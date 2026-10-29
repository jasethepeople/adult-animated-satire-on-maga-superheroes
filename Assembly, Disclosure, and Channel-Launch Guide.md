# Assembly, Disclosure, and Channel-Launch Guide

> **Legal and platform note:** This is a working production guide, not legal advice. Before release, have a qualified media/IP attorney review the final episodes, channel branding, voice choices, and monetization plan. Platform policies and AI-tool terms change, so confirm the current rules directly before each launch.

## 1. Assemble the Proof of Concept

Pandora AI should be treated as a source of short visual shots, not as the editor for the entire episode. The approved ten-shot test sequence should be assembled in a non-linear editor after the audio is recorded. This preserves timing, enables replacement of weak shots, and reduces the need to regenerate a complete sequence when only one visual moment fails.

| Step | Deliverable | Practical direction |
| --- | --- | --- |
| 1. Audio lock | One final voiceover WAV/AIFF and dialogue transcript | Record dialogue first. Use different, non-imitative character voices; do not clone or imitate the voice of a real public figure. |
| 2. Reference lock | Two approved character sheets, one background, one hologram prop | Store as `R1–R4`. Do not change reference images mid-sequence. |
| 3. Shot generation | Ten source clips from the shot script | Retain source filename, prompt, seed (if available), output date, and reference images used. |
| 4. Selects | One preferred take per shot plus one backup | Reject any shot with anatomy distortion, unintended readable text, real-world branding, or character drift. |
| 5. Picture edit | 75–90 second timeline | Use reaction shots and cutaways over dialogue to avoid obvious mouth-sync defects. |
| 6. Sound pass | Dialogue, room tone, rain, thunder, spectral hum, music | Keep sound effects low under speech. Use music and effects licensed for the intended distribution and monetization. |
| 7. Titles and notice | Editor-added title card and parody notice | Add text in the editing program, not in the generative model, to control spelling and duration. |
| 8. Export and archive | High-quality master plus upload version | Retain the master, project file, source clips, audio licenses, and prompt log. |

## 2. Recommended Folder Structure

Use a simple, repeatable archive structure from the pilot onward. It allows a shot to be regenerated months later without losing its prompt, reference, or usage history.

```text
AHL_ProofOfConcept/
  01_Script/
  02_Audio/
  03_References/
     R1_CommanderInChief/
     R2_SpectralMentor/
     R3_EstateOffice/
     R4_Hologram/
  04_Pandora_Generations/
     S01/
     S02/
     ...
  05_Selects/
  06_Edit_Project/
  07_Graphics/
  08_Licenses_and_Releases/
  09_Exports/
  10_Prompt_Log/
```

## 3. Prompt and Asset Log

Keep a record for every final shot. It protects production continuity, allows iteration, and creates a defensible record of what was generated and edited.

| Field | Example |
| --- | --- |
| Episode / sequence / shot | `POC / The Warning / S06` |
| Final source filename | `AHL_POC_S06_take03.mp4` |
| Date generated | `YYYY-MM-DD` |
| Pandora mode and settings | Record exact labels shown in the interface |
| Source prompt | Copy unchanged from the shot script, then record any revision |
| Negative prompt | Copy actual value used |
| References attached | `R1, R2, R3` |
| Seed / variation identifier | Record if Pandora supplies it |
| Approval status | `Selected / Backup / Rejected` |
| Reason for selection | `Best costume continuity; clean ending hold` |
| Rights check | `Commercial-use terms checked on YYYY-MM-DD` |

## 4. Required On-Screen and Description Disclosures

Use clear, brief disclosure language. It should be visible to a casual viewer without making the trailer feel like a legal filing.

### End Card

```text
Fictional animated parody.
Characters are exaggerated caricatures in an alternate superhero universe.
Not factual reporting or endorsement.
```

### Video Description Opening

```text
This is an original adult animated political parody. It uses fictionalized cartoon caricatures in an alternate superhero universe. It is not news, factual reporting, or an endorsement by any depicted person or organization. Visuals were created and edited with AI-assisted tools and traditional post-production.
```

### Channel Bio

```text
Original adult animated political parody in an alternate superhero universe. Fictional caricatures, absurd villains, and dry humor. Not affiliated with, authorized by, or endorsed by any person or organization depicted.
```

## 5. YouTube Upload Readiness

YouTube says creators must disclose AI-generated or meaningfully altered content when it is realistic enough to make a real person appear to say or do something they did not do, alters footage of real events or places, or creates a realistic event that did not occur. The upload flow includes an AI-use disclosure setting, and YouTube may show AI labels; failure to make required disclosures can lead to labels or enforcement. [1]

For this project, the visual plan should remain overtly stylized and non-photorealistic. Nevertheless, the production team should review the **AI use** field on every upload and use clear written disclosure in the description. If an episode or promotional clip becomes realistic, uses a recognizable voice imitation, or could plausibly be mistaken for real footage, disclose it through the YouTube upload setting.

YouTube also prohibits misleading impersonation, including AI-generated likeness or voice that falsely suggests the person owns, authorizes, or endorses the channel. The policy specifically notes that parody and well-known public figures can affect its evaluation, but disclosure does not itself excuse impersonation. [2]

| Upload field | Recommended entry for this project |
| --- | --- |
| Channel name | `American Heroes League — Animated Parody` |
| Handle | Choose a distinct handle that does not imitate any person, organization, campaign, or existing channel |
| Banner | Original logo and fictional character art; no copied official seals, campaign marks, or broadcaster branding |
| Description | Use the disclosure opening above, then episode synopsis and credits |
| AI disclosure | Review during each upload; disclose where the content meets the platform requirement or could be mistaken as realistic |
| Thumbnail | Original cartoon still with minimal editor-added text, no fabricated news framing or “real footage” implication |
| Audience | Mark according to actual content; an adult-satire channel should not be framed as children’s programming |

## 6. X Account Readiness

X’s authenticity policy permits compliant Parody, Commentary, and Fan accounts when their purpose is to discuss, satirize, or share information. It prohibits deceptive impersonation and manipulated media that could create widespread confusion on public issues or cause serious harm. [3]

Create a transparent brand account rather than an account styled as any public figure. Use a distinct original profile image, original banner art, and a name that visibly signals parody. Do not post clips as if they were real statements, actual endorsements, or genuine news footage.

| Profile element | Recommended approach |
| --- | --- |
| Display name | `American Heroes League — Parody` |
| Handle | A clearly original series handle, not a variation of a public figure’s name |
| Bio | Use the channel bio above plus `AI-assisted animated satire` |
| Pinned post | “This account publishes fictional adult animated political parody. No post is a real statement, endorsement, or news report.” |
| Posting style | Share short clips, stills, and production updates with the consistent `#AnimatedParody` series tag |
| Account designation | Use any available parody/commentary/fan labeling feature and review the platform’s latest PCF instructions before publishing |

## 7. Rumble and BitChute Readiness

For Rumble and BitChute, use the same transparent title, bio, and description notice. Before uploading, read the platform’s then-current community rules, copyright process, terms of use, AI-content rules, and monetization terms directly in the account interface. Do not assume another platform’s disclosure or parody approach automatically transfers.

| Platform | Recommended role | Publishing practice |
| --- | --- | --- |
| Rumble | Full episode and premiere hub | Publish the final edit with the standard parody notice and full credits. Keep title, thumbnail, and description clearly fictional. |
| BitChute | Secondary archive / alternative audience channel | Use the same master and disclosure. Maintain a prompt/asset log in case of content or copyright queries. |
| YouTube | Discovery, trailers, edited episodes | Use the upload checklist above and avoid misleading channel/voice presentation. |
| X | Short-form discovery and community discussion | Lead to the full episode with a conspicuous parody statement in the post and profile. |

## 8. Voice and Music Rules for This Series

Use original performances, licensed voice actors, or clearly stylized synthetic voices that do not purport to be real people. Do not present a public figure’s voice as authentic, do not use a soundalike to imply endorsement, and do not combine realistic voice imitation with realistic visual presentation.

Use only music, sound effects, fonts, images, footage, and graphic assets with rights that cover the planned commercial platforms and monetization. Keep licenses, invoices, and attribution requirements in the `08_Licenses_and_Releases` folder.

## 9. Channel-Opening Checklist

Complete this checklist before making any account public.

| Item | Completion standard |
| --- | --- |
| Brand identity | Original series name, original handle, original avatar, original banner, no public-figure or campaign imitation |
| Parody transparency | Profile bio, pinned post, video description, and end card state the project is fictional animated parody |
| Episode metadata | Accurate title, synopsis, credits, AI-assisted disclosure, rights details, and age/audience settings |
| Asset rights | Stored evidence of rights for music, voice, fonts, footage, and graphics |
| AI records | Prompt log, source clips, reference assets, selected takes, and edit project are archived |
| Upload check | Current policy review performed immediately before upload |
| Audience response process | One contact email and a documented process for reviewing claims, removals, or corrections |

## 10. Production Recommendation

Do not create or market all four channels until the 75–90 second proof of concept has passed the continuity test. First, use Pandora AI to generate the two model sheets, four essential reference assets, and the ten-shot sequence. Assemble it, test it privately with a small group, and only then standardize the channel artwork, episode template, and production cadence.

The full 20–22 minute episode should then be built as a collection of short sequences using the same locked references, not as one long generative-video job. If Pandora AI does not sustain character consistency, use it for atmospheric cutaways, transitions, and background plates while using a separate character-animation pipeline for dialogue scenes.

## References

[1]: https://support.google.com/youtube/answer/14328491?hl=en "YouTube Help — Disclosing use of GenAI content"
[2]: https://support.google.com/youtube/answer/2801947?hl=en "YouTube Help — Impersonation policy"
[3]: https://help.x.com/en/rules-and-policies/authenticity "X Help Center — Authenticity"
